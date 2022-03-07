from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import numpy as np


def function_age(age):
    try:
        age = int(age)
        if age < 18:
            return None
        elif age < 25:
            return -0.95197
        elif age < 35:
            return -0.07854
        elif age < 45:
            return 0.49788
        elif age < 55:
            return 1.09449
        elif age < 65:
            return 1.82213
        else:
            return 2.59171
    except:
        return None

def function_gender(gender):
    if gender == "Man":
        return -0.48246
    elif gender == "Woman":
        return 0.48246
    else:
        None

def function_education(education):
    if education == "Left school before 16 years":
        return -2.43591
    elif education == "Left school at 16 years":
        return -1.73790
    elif education == "Left school at 17 years":
        return -1.43719
    elif education == "Left school at 18 years":
        return -1.22751
    elif education == "Some college or university, no certificate or degree":
        return -0.61113
    elif education == "Professional certificate/ diploma":
        return -0.05921
    elif education == "University degree":
        return 0.45468
    elif education == "Master's degree":
        return 1.16365
    elif education == "Doctoral degree":
        return 1.98437
    else:
        None

def function_country(country):
    if country == 'Australia':
        return [1,0,0,0,0,0,0]
    elif country == 'Canada':
        return [0,1,0,0,0,0,0]
    elif country == 'New Zealand':
        return [0,0,1,0,0,0,0]
    elif country == 'Other':
        return [0,0,0,1,0,0,0]
    elif country == 'Republic of Ireland':
        return [0,0,0,0,1,0,0]
    elif country == 'UK':
        return [0,0,0,0,0,1,0]
    elif country == 'USA':
        return [0,0,0,0,0,0,1]
    else:
        None

def function_ethnicity(ethnicity):
    if ethnicity == "Asian":
        return [1,0,0,0,0,0,0]
    elif ethnicity == "Black":
        return [0,1,0,0,0,0,0]
    elif ethnicity == "Mixed-Black/Asian":
        return [0,0,1,0,0,0,0]
    elif ethnicity == "Mixed-White/Asian":
        return [0,0,0,1,0,0,0]
    elif ethnicity == "Mixed-White/Black":
        return [0,0,0,0,1,0,0]
    elif ethnicity == "Other":
        return [0,0,0,0,0,1,0]
    elif ethnicity == "White":
        return [0,0,0,0,0,0,1]
    else:
        None

def function_nscore(nscore):
    nscore = int(nscore)
    if nscore == 12:
        return -3.46436
    elif nscore == 13:
        return -3.15735
    elif nscore == 14:
        return -2.75696
    elif nscore == 15:
        return -2.52197
    elif nscore == 16:
        return -2.42317
    elif nscore == 17:
        return -2.34360
    elif nscore == 18:
        return -2.21844
    elif nscore == 19:
        return -2.05048
    elif nscore == 20:
        return -1.86962
    elif nscore == 21:
        return -1.69163
    elif nscore == 22:
        return -1.55078
    elif nscore == 23:
        return -1.43907
    elif nscore == 24:
        return -1.32828
    elif nscore == 25:
        return -1.19430
    elif nscore == 26:
        return -1.05308
    elif nscore == 27:
        return -0.92104
    elif nscore == 28:
        return -0.79151
    elif nscore == 29:
        return -0.67825
    elif nscore == 30:
        return -0.58016
    elif nscore == 31:
        return -0.46725
    elif nscore == 32:
        return -0.34799
    elif nscore == 33:
        return -0.24649
    elif nscore == 34:
        return -0.14882
    elif nscore == 35:
        return -0.05188
    elif nscore == 36:
        return 0.04257
    elif nscore == 37:
        return 0.13606
    elif nscore == 38:
        return 0.22393
    elif nscore == 39:
        return 0.31287
    elif nscore == 40:
        return 0.41667
    elif nscore == 41:
        return 0.52135
    elif nscore == 42:
        return 0.62967
    elif nscore == 43:
        return 0.73545
    elif nscore == 44:
        return 0.82562
    elif nscore == 45:
        return 0.91093
    elif nscore == 46:
        return 1.02119
    elif nscore == 47:
        return 1.13281
    elif nscore == 48:
        return 1.23461
    elif nscore == 49:
        return 1.37297 
    elif nscore == 50:
        return 1.49158
    elif nscore == 51:
        return 1.60383
    elif nscore == 52:
        return 1.72012
    elif nscore == 53:
        return 1.83990
    elif nscore == 54:
        return 1.98437
    elif nscore == 55:
        return 2.12700
    elif nscore == 56:
        return 2.28554
    elif nscore == 57:
        return 2.46262
    elif nscore == 58:
        return 2.61139
    elif nscore == 59:
        return 2.82196
    elif nscore == 60:
        return 3.27393
    else:
        None

def function_escore(escore):
    escore = int(escore)
    if escore == 16:
        return -3.27393
    elif escore == 17:
        return -3.17537
    elif escore == 18:
        return -3.00537
    elif escore == 19:
        return -2.72827
    elif escore == 20:
        return -2.53830
    elif escore == 21:
        return -2.44904
    elif escore == 22:
        return -2.32338
    elif escore == 23:
        return -2.21069
    elif escore == 24:
        return -2.11437
    elif escore == 25:
        return -2.03972
    elif escore == 26:
        return -1.92173
    elif escore == 27:
        return -1.76250
    elif escore == 28:
        return -1.63340
    elif escore == 29:
        return -1.50796
    elif escore == 30:
        return -1.37639
    elif escore == 31:
        return -1.23177
    elif escore == 32:
        return -1.09207
    elif escore == 33:
        return -0.94779
    elif escore == 34:
        return -0.80615
    elif escore == 35:
        return -0.69509
    elif escore == 36:
        return -0.57545
    elif escore == 37:
        return -0.43999
    elif escore == 38:
        return -0.30033
    elif escore == 39:
        return -0.15487
    elif escore == 40:
        return 0.00332
    elif escore == 41:
        return 0.16767
    elif escore == 42:
        return 0.32197
    elif escore == 43:
        return 0.47617
    elif escore == 44:
        return 0.63779
    elif escore == 45:
        return 0.80523
    elif escore == 46:
        return 0.96248
    elif escore == 47:
        return 1.11406
    elif escore == 48:
        return 1.28610
    elif escore == 49:
        return 1.45421
    elif escore == 50:
        return 1.58487
    elif escore == 51:
        return 1.74091
    elif escore == 52:
        return 1.93886
    elif escore == 53:
        return 2.12700
    elif escore == 54:
        return  2.32338
    elif escore == 55:
        return 2.57309
    elif escore == 56:
        return 2.85950
    elif escore == 57:
        return 2.92000
    elif escore == 58:
        return 3.00537
    elif escore == 59:
        return 3.27393
    else:
        None

def function_oscore(oscore):
    oscore = int(oscore)
    if oscore == 24:
        return -3.27393
    elif oscore == 25:
        return -3.06672
    elif oscore == 26:
        return -2.85950
    elif oscore == 27:
        return -2.74575
    elif oscore == 28:
        return -2.63199
    elif oscore == 29:
        return -2.39883
    elif oscore == 30:
        return -2.21069
    elif oscore == 31:
        return -2.09015
    elif oscore == 32:
        return -1.97495
    elif oscore == 33:
        return -1.82919
    elif oscore == 34:
        return -1.68062
    elif oscore == 35:
        return -1.55521
    elif oscore == 36:
        return -1.42424
    elif oscore == 37:
        return -1.27553
    elif oscore == 38:
        return -1.11902
    elif oscore == 39:
        return  -0.97631
    elif oscore == 40:
        return -0.84732
    elif oscore == 41:
        return -0.71727
    elif oscore == 42:
        return -0.58331
    elif oscore == 43:
        return -0.45174
    elif oscore == 44:
        return -0.31776
    elif oscore == 45:
        return -0.17779
    elif oscore == 46:
        return -0.01928
    elif oscore == 47:
        return 0.14143
    elif oscore == 48:
        return 0.29338
    elif oscore == 49:
        return 0.44585
    elif oscore == 50:
        return 0.58331
    elif oscore == 51:  
        return 0.72330
    elif oscore == 52:
        return 0.88309
    elif oscore == 53:
        return 1.06238
    elif oscore == 54:
        return 1.24033
    elif oscore == 55:
        return 1.43533
    elif oscore == 56:
        return 1.65653
    elif oscore == 57:
        return 1.88511
    elif oscore == 58:
        return 2.15324
    elif oscore == 59:
        return 2.44904
    elif oscore == 60:
        return 2.90161
    else:
        None

def function_ascore(ascore):
    ascore = int(ascore)
    if ascore == 12:
        return -3.46436
    elif ascore == 13:
        return -3.40735
    elif ascore == 14:
        return -3.32983
    elif ascore == 15:
        return -2.24197
    elif ascore == 16:
        return -3.15735
    elif ascore == 17:
        return -3.07848
    elif ascore == 18:
        return -3.00537
    elif ascore == 19:
        return -2.98131
    elif ascore == 20:
        return -2.96622
    elif ascore == 21:
        return -2.94203
    elif ascore == 22:
        return -2.92083
    elif ascore == 23:
        return -2.90161
    elif ascore == 24:
        return -2.78793 
    elif ascore == 25:
        return -2.70172 
    elif ascore == 26:
        return -2.53830 
    elif ascore == 27:
        return -2.35413 
    elif ascore == 28:
        return -2.21844 
    elif ascore == 29:
        return -2.07848 
    elif ascore == 30:
        return -1.92595
    elif ascore == 31:
        return -1.77200 
    elif ascore == 32:
        return -1.62090 
    elif ascore == 33:
        return -1.47955 
    elif ascore == 34:
        return -1.34289 
    elif ascore == 35:
        return -1.21213
    elif ascore == 36:
        return -1.07533 
    elif ascore == 37:
        return -0.91699
    elif ascore == 38:
        return -0.76096
    elif ascore == 39:
        return -0.60633
    elif ascore == 40:
        return -0.45321
    elif ascore == 41:
        return -0.30172 
    elif ascore == 42:
        return -0.15487 
    elif ascore == 43:
        return -0.01729 
    elif ascore == 44:
        return 0.13136 
    elif ascore == 45:
        return 0.28783 
    elif ascore == 46:
        return 0.43852 
    elif ascore == 47:
        return 0.59042
    elif ascore == 48:
        return 0.76096
    elif ascore == 49:
        return 0.94156
    elif ascore == 50:
        return 1.11406
    elif ascore == 51:
        return 1.28610
    elif ascore == 52:
        return 1.45039
    elif ascore == 53:
        return 1.61108
    elif ascore == 54:
        return 1.81866
    elif ascore == 55:
        return 2.03972
    elif ascore == 56:
        return 2.23427
    elif ascore == 57:
        return 2.46262
    elif ascore == 58:
        return 2.75696
    elif ascore == 59:
        return 3.15735
    elif ascore == 60:
        return 3.46436
    else:
        None

def function_cscore(cscore):
    cscore = int(cscore)
    if cscore == 17:
        return -3.46436
    elif cscore == 18:
        return -3.31086
    elif cscore == 19:
        return -3.15735
    elif cscore == 20:
        return -2.90161
    elif cscore == 21:
        return -2.72827
    elif cscore == 22:
        return -2.57309
    elif cscore == 23:
        return -2.42317
    elif cscore == 24:
        return -2.30408
    elif cscore == 25:
        return -2.18109
    elif cscore == 26:
        return -2.04506
    elif cscore == 27:
        return -1.92173
    elif cscore == 28:
        return -1.78169
    elif cscore == 29:
        return -1.64101
    elif cscore == 30:
        return -1.51840
    elif cscore == 31:
        return -1.38502
    elif cscore == 32:
        return -1.25773
    elif cscore == 33:
        return -1.13788
    elif cscore == 34:
        return -1.01450
    elif cscore == 35:
        return -0.89891
    elif cscore == 36:
        return -0.78155
    elif cscore == 37:
        return -0.65253 
    elif cscore == 38:
        return -0.52745 
    elif cscore == 39:
        return -0.40581
    elif cscore == 40:
        return -0.27607 
    elif cscore == 41:
        return -0.14277  
    elif cscore == 42:
        return -0.00665  
    elif cscore == 43:
        return 0.12331  
    elif cscore == 44:
        return 0.25953  
    elif cscore == 45:
        return 0.41594 
    elif cscore == 46:
        return 0.58489 
    elif cscore == 47:
        return 0.75830
    elif cscore == 48:
        return 0.93949
    elif cscore == 49:
        return 1.13407
    elif cscore == 50:
        return 1.30612
    elif cscore == 51:
        return 1.46191
    elif cscore == 52:
        return 1.63088
    elif cscore == 53:
        return 1.81175
    elif cscore == 54:
        return 2.04506
    elif cscore == 55:
        return 2.33337
    elif cscore == 56:
        return 2.63199
    elif cscore == 57:
        return 3.00537
    else:
        None

def function_impulsivity(impulsivity):
    impulsivity = int(impulsivity)
    if impulsivity == 1:
        return -2.55524
    elif impulsivity == 2:
        return -1.37983
    elif impulsivity == 3:
        return -0.71126
    elif impulsivity == 4:
        return -0.21712
    elif impulsivity == 5:
        return 0.19268
    elif impulsivity == 6:
        return 0.52975
    elif impulsivity == 7:
        return 0.88113
    elif impulsivity == 8:
        return 1.29221
    elif impulsivity == 9:
        return 1.86203
    elif impulsivity == 10:
        return 2.90161
    else:
        None

def function_SS(SS):
    SS = int(SS)
    if SS == 1:
        return -2.07848
    elif SS == 2:
        return -1.54858
    elif SS == 3:
        return -1.18084
    elif SS == 4:
        return -0.84637
    elif SS == 5:
        return -0.52593
    elif SS == 6:
        return -0.21575
    elif SS == 7:
        return 0.07987
    elif SS == 8:
        return 0.40148
    elif SS == 9:
        return 0.76540
    elif SS == 10:
        return 1.22470
    elif SS == 11:
        return 1.92173
    else:
        None

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            drugs = ['Alcohol','Amphet','Amyl','Benzos','Caff','Cannabis','Coke','Crack','Ecstasy','Heroin','Ketamine','Legalh','LSD','Meth','Mushrooms','Nicotine','VSA']
            results_monthly_addicted = {
                "Alcohol":{0: "Not addicted", 1: "Addicted"},
                "Cannabis": {0: "Not addicted", 1: "Addicted"},
                "Nicotine":{0: "Not addicted", 1: "Addicted"},
                "Amphet":{0: "Not addicted", 1: "Addicted"},
                "Benzos":{0: "Not addicted", 1: "Addicted"},
                "Coke": {0: "Not addicted", 1: "Addicted"},
                "Ecstasy": {0: "Not addicted", 1: "Addicted"},
                "Legalh":{0: "Not addicted", 1: "Addicted"}
            }
            results_used = {
                "Amyl":{0: "Never used", 1: "Used"}, 
                "Crack":{0: "Never used", 1: "Used"}, 
                "Heroin":{0: "Never used", 1: "Used"}, 
                "Ketamine":{0: "Never used", 1: "Used"}, 
                "Meth":{0: "Never used", 1: "Used"}, 
                "VSA":{0: "Never used", 1: "Used"},
                "LSD":{0: "Never used", 1: "Used"},
                "Mushrooms":{0: "Never used", 1: "Used"}
            }
            results_daily = {
                "Caff":{0: "Not daily addicted", 1: "Daily addicted"}
            }

            # get sound from request
            age = function_age(request.GET.get('age'))
            gender = function_gender(request.GET.get('gender'))
            education = function_education(request.GET.get('education'))
            country = function_country(request.GET.get('country'))
            ethnicity = function_ethnicity(request.GET.get('ethnicity'))
            nscore = function_nscore(request.GET.get('nscore'))
            escore = function_escore(request.GET.get('escore'))
            oscore = function_oscore(request.GET.get('oscore'))
            ascore = function_ascore(request.GET.get('ascore'))
            cscore = function_cscore(request.GET.get('cscore'))
            impulsivity = function_impulsivity(request.GET.get('impulsivity'))
            SS = function_SS(request.GET.get('SS'))

            vector = [age, gender, education] + country + ethnicity + [nscore, escore, oscore, ascore, cscore, impulsivity, SS]
            vector = np.array([vector])

            # predict based on vector
            prediction_alcohol = PredictorConfig.alcohol.predict(vector)[0]
            prediction_amphet = PredictorConfig.amphet.predict(vector)[0]
            prediction_amyl = PredictorConfig.amyl.predict(vector)[0]
            prediction_benzos = PredictorConfig.benzos.predict(vector)[0]
            prediction_caff = PredictorConfig.caff.predict(vector)[0]
            prediction_cannabis = PredictorConfig.cannabis.predict(vector)[0]
            prediction_coke = PredictorConfig.coke.predict(vector)[0]
            prediction_crack = PredictorConfig.crack.predict(vector)[0]
            prediction_ecstasy = PredictorConfig.ecstasy.predict(vector)[0]
            prediction_heroin = PredictorConfig.heroin.predict(vector)[0]
            prediction_ketamine = PredictorConfig.ketamine.predict(vector)[0]
            prediction_legalh = PredictorConfig.legalh.predict(vector)[0]
            prediction_lsd = PredictorConfig.lsd.predict(vector)[0]
            prediction_meth = PredictorConfig.meth.predict(vector)[0]
            prediction_mushrooms = PredictorConfig.mushrooms.predict(vector)[0]
            prediction_nicotine = PredictorConfig.nicotine.predict(vector)[0]
            prediction_vsa = PredictorConfig.vsa.predict(vector)[0]
            
            predictions = [prediction_alcohol,prediction_amphet,prediction_amyl,prediction_benzos,prediction_caff,prediction_cannabis,prediction_coke,prediction_crack,prediction_ecstasy,prediction_heroin,prediction_ketamine,prediction_legalh,prediction_lsd,prediction_meth,prediction_mushrooms,prediction_nicotine,prediction_vsa]
            
            # build response
            response = {drug: results_monthly_addicted[drug][pred] if drug in results_monthly_addicted.keys() else results_used[drug][pred] if drug in results_used.keys() else results_daily[drug][pred] for drug, pred in zip(drugs, predictions)}
            # return response
            #return JsonResponse(response)
            return render(request, 'result.html', context=response)


class call_api(APIView):
    def get(self,request):
        if request.method == 'GET':
            drugs = ['Alcohol','Amphet','Amyl','Benzos','Caff','Cannabis','Coke','Crack','Ecstasy','Heroin','Ketamine','Legalh','LSD','Meth','Mushrooms','Nicotine','VSA']
            results_monthly_addicted = {
                "Alcohol":{0: "Not addicted", 1: "Addicted"},
                "Cannabis": {0: "Not addicted", 1: "Addicted"},
                "Nicotine":{0: "Not addicted", 1: "Addicted"},
                "Amphet":{0: "Not addicted", 1: "Addicted"},
                "Benzos":{0: "Not addicted", 1: "Addicted"},
                "Coke": {0: "Not addicted", 1: "Addicted"},
                "Ecstasy": {0: "Not addicted", 1: "Addicted"},
                "Legalh":{0: "Not addicted", 1: "Addicted"}
            }
            results_used = {
                "Amyl":{0: "Never used", 1: "Used"}, 
                "Crack":{0: "Never used", 1: "Used"}, 
                "Heroin":{0: "Never used", 1: "Used"}, 
                "Ketamine":{0: "Never used", 1: "Used"}, 
                "Meth":{0: "Never used", 1: "Used"}, 
                "VSA":{0: "Never used", 1: "Used"},
                "LSD":{0: "Never used", 1: "Used"},
                "Mushrooms":{0: "Never used", 1: "Used"}
            }
            results_daily = {
                "Caff":{0: "Not daily addicted", 1: "Daily addicted"}
            }

            # get sound from request
            age = function_age(request.GET.get('age'))
            gender = function_gender(request.GET.get('gender'))
            education = function_education(request.GET.get('education'))
            country = function_country(request.GET.get('country'))
            ethnicity = function_ethnicity(request.GET.get('ethnicity'))
            nscore = function_nscore(request.GET.get('nscore'))
            escore = function_escore(request.GET.get('escore'))
            oscore = function_oscore(request.GET.get('oscore'))
            ascore = function_ascore(request.GET.get('ascore'))
            cscore = function_cscore(request.GET.get('cscore'))
            impulsivity = function_impulsivity(request.GET.get('impulsivity'))
            SS = function_SS(request.GET.get('SS'))

            if (age==None) or (gender==None) or (education==None) or (country==None) or (ethnicity==None) or (nscore==None) or (escore==None) or (oscore==None) or (ascore==None) or (cscore==None) or (impulsivity==None) or (SS==None):
               return JsonResponse(
                    {"api": "Bad request, please check your input"}, 
                    status=400
                ) 
            else:
                vector = [age, gender, education] + country + ethnicity + [nscore, escore, oscore, ascore, cscore, impulsivity, SS]
                vector = np.array([vector])

                # predict based on vector
                prediction_alcohol = PredictorConfig.alcohol.predict(vector)[0]
                prediction_amphet = PredictorConfig.amphet.predict(vector)[0]
                prediction_amyl = PredictorConfig.amyl.predict(vector)[0]
                prediction_benzos = PredictorConfig.benzos.predict(vector)[0]
                prediction_caff = PredictorConfig.caff.predict(vector)[0]
                prediction_cannabis = PredictorConfig.cannabis.predict(vector)[0]
                prediction_coke = PredictorConfig.coke.predict(vector)[0]
                prediction_crack = PredictorConfig.crack.predict(vector)[0]
                prediction_ecstasy = PredictorConfig.ecstasy.predict(vector)[0]
                prediction_heroin = PredictorConfig.heroin.predict(vector)[0]
                prediction_ketamine = PredictorConfig.ketamine.predict(vector)[0]
                prediction_legalh = PredictorConfig.legalh.predict(vector)[0]
                prediction_lsd = PredictorConfig.lsd.predict(vector)[0]
                prediction_meth = PredictorConfig.meth.predict(vector)[0]
                prediction_mushrooms = PredictorConfig.mushrooms.predict(vector)[0]
                prediction_nicotine = PredictorConfig.nicotine.predict(vector)[0]
                prediction_vsa = PredictorConfig.vsa.predict(vector)[0]
                
                predictions = [prediction_alcohol,prediction_amphet,prediction_amyl,prediction_benzos,prediction_caff,prediction_cannabis,prediction_coke,prediction_crack,prediction_ecstasy,prediction_heroin,prediction_ketamine,prediction_legalh,prediction_lsd,prediction_meth,prediction_mushrooms,prediction_nicotine,prediction_vsa]
                    
                # build response
                response = {drug: results_monthly_addicted[drug][pred] if drug in results_monthly_addicted.keys() else results_used[drug][pred] if drug in results_used.keys() else results_daily[drug][pred] for drug, pred in zip(drugs, predictions)}
                # return response
                return JsonResponse(response)
            

def drug_test(request):
    return render(request, 'test.html')

def home(request):
    return render(request, 'home.html')