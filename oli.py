import csv
import numpy

from pylab import *

attributeNames = [
'communityname','State','countyCode','communityCode','fold','pop','perHoush','pctBlack','pctWhite','pctAsian','pctHisp','pct12-21','pct12-29','pct16-24','pct65up','persUrban','pctUrban','medIncome','pctWwage','pctWfarm','pctWdiv','pctWsocsec','pctPubAsst','pctRetire','medFamIncome','perCapInc','whitePerCap','blackPerCap','NAperCap','asianPerCap','otherPerCap','hispPerCap','persPoverty','pctPoverty','pctLowEdu','pctNotHSgrad','pctCollGrad','pctUnemploy','pctEmploy','pctEmployMfg','pctEmployProfServ','pctOccupManu','pctOccupMgmt','pctMaleDivorc','pctMaleNevMar','pctFemDivorc','pctAllDivorc','persPerFam','pct2Par','pctKids2Par','pctKids-4w2Par','pct12-17w2Par','pctWorkMom-6','pctWorkMom-18','kidsBornNevrMarr','pctKidsBornNevrMarr','numForeignBorn','pctFgnImmig-3','pctFgnImmig-5','pctFgnImmig-8','pctFgnImmig-10','pctImmig-3','pctImmig-5','pctImmig-8','pctImmig-10','pctSpeakOnlyEng','pctNotSpeakEng','pctLargHousFam','pctLargHous','persPerOccupHous','persPerOwnOccup','persPerRenterOccup','pctPersOwnOccup','pctPopDenseHous','pctSmallHousUnits','medNumBedrm','houseVacant','pctHousOccup','pctHousOwnerOccup','pctVacantBoarded','pctVacant6up','medYrHousBuilt','pctHousWOphone','pctHousWOplumb','ownHousLowQ','ownHousMed','ownHousUperQ','ownHousQrange','rentLowQ','rentMed','rentUpperQ','rentQrange','medGrossRent','medRentpctHousInc','medOwnCostpct','medOwnCostPctWO','persEmergShelt','persHomeless','pctForeignBorn','pctBornStateResid','pctSameHouse-5','pctSameCounty-5','pctSameState-5','numPolice','policePerPop','policeField','policeFieldPerPop','policeCalls','policCallPerPop','policCallPerOffic','policePerPop2','racialMatch','pctPolicWhite','pctPolicBlack','pctPolicHisp','pctPolicAsian','pctPolicMinority','officDrugUnits','numDiffDrugsSeiz','policAveOT','landArea','popDensity','pctUsePubTrans','policCarsAvail','policOperBudget','pctPolicPatrol','gangUnit','pctOfficDrugUnit','policBudgetPerPop','murders','murdPerPop','rapes','rapesPerPop','robberies','robbbPerPop','assaults','assaultPerPop','burglaries','burglPerPop','larcenies','larcPerPop','autoTheft','autoTheftPerPop','arsons','arsonsPerPop','violentPerPop','nonViolPerPop',
]

# read data from comma-separated datafile
csvfile = open('data/communities.data')
csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

# read each row, discarding first DISCARD columns
DISCARD = 5
rows = [row[DISCARD:] for row in list(csvreader)]

# count matrix dimensions
#X data matrix, rows correspond to N data objects, each of which contains M attributes
# y (Nx1) class index: for each data object, y contains a class index, y in {0,1,...,C-1} where C is number of classes
#attributeNames Mx1
#classNames Cx1
M = len(rows[1]) # number of attributes
N = len(rows)    # number of data objects
# C number of classes

# initialize numpy matrix (better performance over regular python 2D arrays)
X = numpy.zeros(shape=(N,M))

# find columns with unknowns
X_missing = numpy.zeros(shape=(N,M));
listlol =  [1 if cell == '?' else 0 for cell in row for row in rows]
X_missing.flat[:] = listlol

unknown_columns = set();
for i,row in enumerate(rows):
    for j,cell in enumerate(row):
        if cell == '?':
            unknown_columns.add(j)
        else:
            rows[i][j] = float(cell)

means = {}
for c in unknown_columns:
    summed = 0;
    n = 0;
    for r in rows:
        if r[c] != '?':
            summed += r[c]
            n += 1
    means[c] = summed / n

for i,row in enumerate(rows):
    for j,cell in enumerate(row):
        if cell == '?':
            row[j] = means[j] # mean?
    X[i,:] = row

## P C fucking A
#subtract mean
Y = X - numpy.ones((N,1))*X.mean(0)
#PCA by computing SVD of Y
U,S,V = linalg.svd(Y,full_matrices=False)


# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 


V = mat(V).T

# Project the centered data onto principal component space
Z = Y * V


# Indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA of the data
figure()
title('PCAAAAAAAAAAAAA')
plot(Z[:,i], Z[:,j], 'o')

# Output result to screen
show()
