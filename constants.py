airport_code_location_data_file = 'Dataset/airport-code-to-location.csv'
test_medium_flight = 'Dataset/Medium/fake_flights_data_2.csv'
test_medium_PNR = 'Dataset/Medium/Double_leg.csv'
test_small_flight = 'Dataset/Small/Mock_Flight_Inv.csv'
test_small_PNR = 'Dataset/Small/Double_leg.csv'
test_large_PNR = 'Dataset/Large/large_PNR.csv'
test_large_flight = 'Dataset/Large/large_Flights.csv'
# Change the path of test_flight_data_file and test_PNR_data_file according to the size of data_file
test_flight_data_file = test_small_flight 
test_PNR_data_file = test_small_PNR
n_cabin=2

ETD=72
cabinScoreFirst=1950
cabinScoreBusiness=1800
cabinScorePremium=1700
cabinScoreEconomy=1592
MCT=1
MAXCT=12
PNR_SSR={'grade1':250,'grade2':150}
loyalty={'CM':2000,'Platinum':1800,'Gold':1600,'Silver':1500}
PNR_connection=100
PNR_paidservice=200
PNR_bookingtype=500
PNR_pax=50
NON_ASSIGNMENT_COST=100
CITY_PAIR_THRESHOLD=8
weight_flight_map=100
weight_pnr_map=100
weight_cabin_map=100
