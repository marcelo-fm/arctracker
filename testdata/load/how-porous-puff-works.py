out_vol = DarcyFlow(head, poros, thickn, transm, dir1, mag1)
ParticleTrack(dir1, mag1, ttrack.txt, 500, 650, "#", "#", track_feat.shp)
out_puff = PorousPuff(ttrack.txt, poros, thickn, 3.2e7, 50000, 6, 3, 1, 250)