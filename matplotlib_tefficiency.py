# Wrapper around CERN ROOT TEfficiency class
# To make a TEfficiency plot on matplotlib
#  Author: Iacopo Longarini
#  version 0.0





def GetEfficiency(Xtot, Xpass, nBins, binXmin, binXmax):
    """
    version. 0.0
    Stupid implementation
    depends on ROOT
    """
    h_total = ROOT.TH1F("h_total","",nBins,binXmin,binXmax)
    h_pass  = ROOT.TH1F("h_pass","",nBins,binXmin,binXmax)
    h_total.SetDirectory(0)
    h_pass.SetDirectory(0)

    for x in Xtot:
        h_total.Fill(x)
    for x in Xpass:
        h_pass.Fill(x)
        
    te = ROOT.TEfficiency(h_pass,h_total)
    
    gr = te.CreateGraph()
    i_x = ROOT.Double(0)
    i_y = ROOT.Double(0)
    nPoints = gr.GetN()

    #using npy array to avoid overwrite of x and y
    teff = np.zeros((nPoints,5))
    for i in range(nPoints):
        gr.GetPoint(i,i_x,i_y)
        i_ex = gr.GetErrorXlow(i)
        i_eyHi = gr.GetErrorYhigh(i)    
        i_eyLo = gr.GetErrorYlow(i)
        teff[i] = np.array( [i_x,i_y,i_ex,i_eyLo,i_eyHi] )
    
    #Cleanup
    te.IsA().Destructor(te)
    h_total.IsA().Destructor(h_total)
    h_pass.IsA().Destructor(h_pass)
    
    eff = {
        'x'    : teff[:,0],
        'y'    : teff[:,1],
        #'xerr' : teff[:,2],
        'yerr' : [ teff[:,3], teff[:,4] ]
    }
    return eff
