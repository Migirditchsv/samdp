#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:27:14 2020

@author: sam
"""
import samdp
import os  # play gif at end

stateSpace = samdp.stateSpaceGenerator(20, 0.5)

actionPrimatives = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
                    (-1, -1), (1, 1), (-1, 1), (1, -1)]

transitionModel = samdp.transitionModelGenerator(
    stateSpace, actionPrimatives, 0.2)

demo = samdp.SAMDP(stateSpace, actionPrimatives, transitionModel)
demo.renderFrame()

while demo.solverIterations < 60:  # demo.maxDifference > 0.000001:

    demo.hybridIterationStep()
    stepNum = demo.solverIterations

    if stepNum < 10:
        demo.renderFrame()
    elif stepNum < 20 and stepNum % 3 == 0:
        demo.renderFrame()
    elif stepNum < 70 and stepNum % 4 == 0:
        demo.renderFrame()

    if demo.frameBuffer % 20 == 0:
        # One unwritten frame wastes ~10mb of ram, but writing is slow
        demo.writeOutFrameBuffer()

# final frame buffer flush
demo.writeOutFrameBuffer()
# stitch to gif
demo.renderGIF()

# play the resulting gif
os.system('xdg-open out.mp4')
