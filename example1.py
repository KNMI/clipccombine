# python
from clipc_combine_process import clipc_combine_process
from clipc_combine_process import serve_netcdf

# local...
url1 = 'example/vDTR_JUN_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'
url2 = 'example/vDTR_OCT_MPI-M-MPI-ESM-LR_rcp85_r1i1p1_SMHI-RCA4_v1_EUR-11_2006-2100.nc'

#url1= 'http://opendap.knmi.nl/knmi/thredds/dodsC/IS-ENES/TESTSETS/tas_day_EC-EARTH_rcp26_r8i1p1_20760101-21001231.nc'
#url2= 'http://opendap.knmi.nl/knmi/thredds/dodsC/IS-ENES/TESTSETS/tasmax_day_EC-EARTH_rcp26_r8i1p1_20760101-21001231.nc'

nc_combo , url_combo = clipc_combine_process.combine_two_indecies(url1, url2, "+","test.nc")
#nc_combo , url_combo = clipc_combine_process.combine_two_indecies(url1, url2, "+")



serve_netcdf.visualise(url1, url2, url_combo)

