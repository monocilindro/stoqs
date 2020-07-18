#!/usr/bin/env python
'''
Master loader for CANON July (Summer) Campaign 2020
'''

import os
import sys
from datetime import datetime

parentDir = os.path.join(os.path.dirname(__file__), "../")
sys.path.insert(0, parentDir)

from CANON import CANONLoader
import timing

cl = CANONLoader('stoqs_canon_july2020', 'CANON - July 2020',
                 description='July 2020 shipless campaign in Monterey Bay',
                 x3dTerrains={
                   'https://stoqs.mbari.org/x3d/Monterey25_10x/Monterey25_10x_scene.x3d': {
                     'position': '-2822317.31255 -4438600.53640 3786150.85474',
                     'orientation': '0.89575 -0.31076 -0.31791 1.63772',
                     'centerOfRotation': '-2711557.9403829873 -4331414.329506527 3801353.4691465236',
                     'VerticalExaggeration': '10',
                   },
                   'https://stoqs.mbari.org/x3d/Monterey25_1x/Monterey25_1x_src_scene.x3d': {
                     'name': 'Monterey25_1x',
                     'position': '-2822317.31255 -4438600.53640 3786150.85474',
                     'orientation': '0.89575 -0.31076 -0.31791 1.63772',
                     'centerOfRotation': '-2711557.9403829873 -4331414.329506527 3801353.4691465236',
                     'VerticalExaggeration': '1',
                   },
                 },
                 grdTerrain=os.path.join(parentDir, 'Monterey25.grd')
                 )

startdate = datetime(2020, 7, 15)
enddate = datetime(2020, 7, 31)

# default location of thredds and dods data:
cl.tdsBase = 'http://odss.mbari.org/thredds/'
cl.dodsBase = cl.tdsBase + 'dodsC/'

######################################################################
#  GLIDERS
######################################################################
# Glider data files from CeNCOOS thredds server
# L_662a updated parameter names in netCDF file
cl.l_662a_base = 'http://legacy.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.l_662a_files = [ 'OS_Glider_L_662_20200615_TS.nc', ]
cl.l_662a_parms = ['temperature', 'salinity', 'fluorescence','oxygen']
cl.l_662a_startDatetime = startdate
cl.l_662a_endDatetime = enddate

# NPS_34a updated parameter names in netCDF file
## The following loads decimated subset of data telemetered during deployment
cl.nps34a_base = 'http://legacy.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.nps34a_files = [ 'OS_Glider_NPS_G34_20180514_TS.nc' ]
cl.nps34a_parms = ['temperature', 'salinity','fluorescence']
cl.nps34a_startDatetime = startdate
cl.nps34a_endDatetime = enddate

# NPS_29 ##
cl.nps29_base = 'http://legacy.cencoos.org/thredds/dodsC/gliders/Line66/'
cl.nps29_files = [ 'OS_Glider_NPS_G29_20190528_TS.nc' ]
cl.nps29_parms = ['TEMP', 'PSAL', 'FLU2', 'OXYG']
cl.nps29_startDatetime = startdate
cl.nps29_endDatetime = enddate

######################################################################
# Wavegliders
######################################################################
# WG Tex - All instruments combined into one file - one time coordinate
##cl.wg_tex_base = cl.dodsBase + 'CANON_september2013/Platforms/Gliders/WG_Tex/final/'
##cl.wg_tex_files = [ 'WG_Tex_all_final.nc' ]
##cl.wg_tex_parms = [ 'wind_dir', 'wind_spd', 'atm_press', 'air_temp', 'water_temp', 'sal', 'density', 'bb_470', 'bb_650', 'chl' ]
##cl.wg_tex_startDatetime = startdate
##cl.wg_tex_endDatetime = enddate

# WG Hansen - All instruments combined into one file - one time coordinate
cl.wg_Hansen_base = 'http://dods.mbari.org/opendap/data/waveglider/deployment_data/'
cl.wg_Hansen_files = [
                   'wgHansen/20190522/realTime/20190522.nc',
                  ]

cl.wg_Hansen_parms = [ 'wind_dir', 'avg_wind_spd', 'max_wind_spd', 'atm_press', 'air_temp', 'water_temp_float', 'sal_float',  'water_temp_sub',
                     'sal_sub', 'bb_470', 'bb_650', 'chl', 'beta_470', 'beta_650', 'pH', 'O2_conc_float','O2_conc_sub' ] # two ctds (_float, _sub), no CO2
cl.wg_Hansen_depths = [ 0 ]
cl.wg_Hansen_startDatetime = startdate
cl.wg_Hansen_endDatetime = enddate

# WG Tiny - All instruments combined into one file - one time coordinate
cl.wg_Tiny_base = 'http://dods.mbari.org/opendap/data/waveglider/deployment_data/'
cl.wg_Tiny_files = [
                      'wgTiny/20190513/realTime/20190513.nc',
                   ]


cl.wg_Tiny_parms = [ 'wind_dir', 'avg_wind_spd', 'max_wind_spd', 'atm_press', 'air_temp', 'water_temp', 'sal',  'bb_470', 'bb_650', 'chl',
                    'beta_470', 'beta_650', 'pCO2_water', 'pCO2_air', 'pH', 'O2_conc' ]
cl.wg_Tiny_depths = [ 0 ]
cl.wg_Tiny_startDatetime = startdate
cl.wg_Tiny_endDatetime = enddate

######################################################################
#  MOORINGS
######################################################################
cl.m1_base = 'http://dods.mbari.org/opendap/data/ssdsdata/deployments/m1/'
cl.m1_files = [
  '201907/OS_M1_20190729hourly_CMSTV.nc', ]
cl.m1_parms = [
  'eastward_sea_water_velocity_HR', 'northward_sea_water_velocity_HR',
  'SEA_WATER_SALINITY_HR', 'SEA_WATER_TEMPERATURE_HR', 'SW_FLUX_HR', 'AIR_TEMPERATURE_HR',
  'EASTWARD_WIND_HR', 'NORTHWARD_WIND_HR', 'WIND_SPEED_HR'
]

cl.m1_startDatetime = startdate
cl.m1_endDatetime = enddate

# Mooring 0A2
cl.oa2_base = 'http://dods.mbari.org/opendap/data/oa_moorings/deployment_data/OA2/201812/'
cl.oa2_files = [
               'realTime/OA2_201812.nc'
               ]
cl.oa2_parms = [
               'wind_dir', 'avg_wind_spd', 'atm_press', 'air_temp', 'water_temp',
               'sal', 'O2_conc', 'chl', 'pCO2_water', 'pCO2_air', 'pH',
               ]
cl.oa2_startDatetime = startdate
cl.oa2_endDatetime = enddate


# Execute the load
cl.process_command_line()

if cl.args.test:
    cl.stride = 100
elif cl.args.stride:
    cl.stride = cl.args.stride

cl.loadM1()  
cl.loadL_662a()
cl.loadLRAUV('brizo', startdate, enddate, critSimpleDepthTime=0.1, sbd_logs=True)
cl.loadLRAUV('daphne', startdate, enddate, critSimpleDepthTime=0.1, sbd_logs=True)
cl.loadLRAUV('makai', startdate, enddate, critSimpleDepthTime=0.1, sbd_logs=True)
cl.loadLRAUV('tethys', startdate, enddate, critSimpleDepthTime=0.1, sbd_logs=True)
#cl.loadLRAUV('brizo', startdate, enddate)
#cl.loadLRAUV('daphne', startdate, enddate)
#cl.loadLRAUV('makai', startdate, enddate)
#cl.loadLRAUV('tethys', startdate, enddate)
#cl.load_NPS29()   
#cl.load_wg_Tiny()
#cl.load_wg_Hansen()
#cl.load_oa2() 
#cl.loadDorado(startdate, enddate, build_attrs=True)

##cl.loadSubSamples() 

# Add any X3D Terrain information specified in the constructor to the database - must be done after a load is executed
cl.addTerrainResources()

print("All Done.")

