# -*- coding: utf-8 -*-
from sys import platform
import numpy as np
# from src.utils import *
from plyfile import PlyData, PlyElement
from jpype import *
import random
import math


# +
class ComputeTE:
    def __init__(self, setPropertyNum = 6):
        jarLocation = "./infodynamics.jar"
        startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=" + jarLocation)

        # Create a Kraskov TE calculator:
        self.teCalcClass = JPackage("infodynamics.measures.continuous.kraskov").TransferEntropyCalculatorMultiVariateKraskov

        self.teCalc = self.teCalcClass()
        self.teCalc.setProperty(self.teCalcClass.PROP_AUTO_EMBED_METHOD, self.teCalcClass.AUTO_EMBED_METHOD_RAGWITZ)
        #  b. Search range for embedding dimension (k) and delay (tau)
        self.teCalc.setProperty(self.teCalcClass.PROP_K_SEARCH_MAX, str(setPropertyNum))
        self.teCalc.setProperty(self.teCalcClass.PROP_TAU_SEARCH_MAX, str(setPropertyNum))

        # Since we're auto-embedding, no need to supply k, l, k_tau, l_tau here:
        self.teCalc.initialise(2, 2)
    
    def calc(self, data_source, data_desc):
#         print(data_source[:10])
#         print(data_desc[:10])
        self.teCalc.setObservations(data_source, data_desc)
        teSourceToDesc = self.teCalc.computeAverageLocalOfObservations()

        self.teCalc.setObservations(data_desc, data_source)
        teDescToSource = self.teCalc.computeAverageLocalOfObservations()

#         print("source to desc : ", teSourceToDesc)
#         print("desc to source : ", teDescToSource)
        return teSourceToDesc, teDescToSource
# -



# +
# C = ComputeTE()

# +
# import random as r

# data_source = [[r.random()*1000,r.random()*1000] for i in range(1000)]
# data_desc = [d for d in data_source[1:]] + [[0.0,0.0]] # source가 desc를 따라가는 경우
# C.calc(data_source,data_desc)

# -


