# python
# clipc combine process with dispel4py
# combine two netCDFs
# knmi team
# author: andrej / alessandro
# clipc@knmi.nl
#

import netCDF4
import random
import numpy as operator
import wcsrequest
import numpy as np

def defaultCallback(message,percentage):
  print "defaultCallback: "+message

#
# two netCDF files combined by operator into one along all dimmensions, should be same...
#

# two urls opened as netCDF files and combined with operator allong all dimensions
#
#def combine_two_indecies(url1,url2,operation,output,callback=defaultCallback):

  # nc1 = netCDF4.Dataset(url1,'r')

  # nc2 = netCDF4.Dataset(url2,'r')

  # callback("nc1 time received: "+str(netCDF4.num2date( nc1.variables['time'][0] , nc1.variables['time'].units ,calendar='standard')),3)
  # callback("nc2 time received: "+str(netCDF4.num2date( nc2.variables['time'][0] , nc2.variables['time'].units ,calendar='standard')),3)

  # nc_combination , combi_name = combine_two_indecies_netcdf(nc1, nc2, operation, output,callback=callback)

  # callback("combo time received: "+str(netCDF4.num2date( nc_combination.variables['time'][0] , nc_combination.variables['time'].units ,calendar='standard')),3)


  # nc_combination.setncattr('CLIPC_url1' , str(url1))
  # nc_combination.setncattr('CLIPC_url2' , str(url2))
  # nc_combination.setncattr('CLIPC_combination_operator' ,str(operation))

#def combine_two_indecies(url1,url2,operation,output,callback=defaultCallback):

def collect(url):
#print "in collector ",url
  
  nc = netCDF4.Dataset(url,'r')

  return nc;

# def combine_two_indecies_netcdf(netCDF1,netCDF2,operator_symbol,output,callback=defaultCallback):

#   #id data layer (3dims...)
#   variable1 = getTitleNC(netCDF1)

#   variable2 = getTitleNC(netCDF2)

#   #RANDOM NAME FOR NC COMBINE... CHANGE...
#   name = output #'test_combine_'+str(random.getrandbits(128))+'.nc'
#   des  = 'KNMI pywps process combines two climate indecies. clipc@knmi.nl'

#   # define operator functions
#   ops = { "+": operator.add , 
#       "-": operator.subtract, 
#       "*": operator.multiply, 
#       "/": operator.divide  }

#   # parse operator symbol to function
#   op_char = operator_symbol
#   op_func = ops[op_char]
#   #result = op_func(a, b)
#   combi = combine_netcdf.combineNetCDFs( name, netCDF1 , variable1 , netCDF2 , variable2 , des , op_func,callback=callback)
#   return combi , name

def read(nc):
#print "in read ", str(nc)
  variableName = getTitleNC(nc)
  print "TITLE:",variableName

  v[:] = nc.variables[variableName][:]

  # normalisation
  n = v.max()

  return (v, n)

#def write(nc,outName,des):
def write(url,outName,des):
#print "in preprocess nc is     ",str(nc)
  print "in preprocess output is ",outName
  print "in preprocess des       ",des

  nc =  collect(url)

  variable = getTitleNC(nc)

#  print "in preprocess variable name is " , variable

  nc_combo = copyNetCDF( outName , nc , des )


  return (nc_combo, variable)


def combine(  var1, norm1 , var2 , norm2 , operator_symbol ):
#  print "in preprocess ",var1, " ",norm1
#  print "in preprocess ",var2, " ",norm2

  ops = { "+": operator.add , 
          "-": operator.subtract, 
          "*": operator.multiply, 
          "/": operator.divide  }

# nc_combination , combi_name = combine_two_indecies_netcdf(nc1, nc2, operation, output,callback=callback)
# callback("combo time received: "+str(netCDF4.num2date( nc_combination.variables['time'][0] , nc_combination.variables['time'].units ,calendar='standard')),3)
# parse operator symbol to function
  op_char = operator_symbol
  op_func = ops[op_char]

  combo = op_func( np.divide(var1 , norm1) , np.divide( var2 , norm2) )


  return combo


def postprocess(combi_variable,nc_combo_file): #,operation):

  print "in postprocess ", type(combi_variable)

  nc_combo_file[0].variables[nc_combo_file[1]][:]   =  combi_variable

  print "in postprocess ", type(nc_combo_file[0])

  return nc_combo_file

def getTitleNC(nc_fid):
#  print str(nc_fid)
  var = None
  for k1 , v in nc_fid.variables.iteritems():
    if "grid_mapping" in v.ncattrs():
      var = k1
  return var

# def combine_two_indecies_wcs(wcs_url1, 
#   wcs_url2, 
#   operator_symbol, 
#   bbox=None , 
#   time1=None , 
#   time2=None ,
#   output_file1='nc1.nc',
#   output_file2='nc2.nc',
#   output_file3='combine.nc' ,
#   callback=defaultCallback):

#   # wcs combo
#   defaultCallback('Combine Two Web Coverage Service operations with: '+str(operator_symbol),1)
#   defaultCallback('wcs url1: '+str(wcs_url1),1) 
#   defaultCallback('wcs url2: '+str(wcs_url2),1)
#   defaultCallback('bbox:     '+str(bbox),1)
#   defaultCallback('time1:     '+str(time1),1)
#   defaultCallback('time2:     '+str(time2),1)

#   nc1 = wcsrequest.getWCS(wcs_url1, bbox, time1, output_file1,callback=callback)

#   nc2 = wcsrequest.getWCS(wcs_url2, bbox, time2, output_file2,callback=callback)  
  
#   defaultCallback("Combining",2);
  
#   nc_output , nc_out = combine_two_indecies( nc1 , nc2 , operator_symbol , output_file3 ,callback=callback)
  
#   defaultCallback("Combining ready",3);
  
#   nc_output.setncattr('CLIPC_url1' , str(wcs_url1))
#   nc_output.setncattr('CLIPC_url2' , str(wcs_url2))

#   return nc1 , nc2 , nc_out




# end

# copy existing netcdf to new file with name
#
def copyNetCDF(name, nc_fid , des ):

  w_nc_fid = netCDF4.Dataset(name, 'w', format='NETCDF4')

  w_nc_fid.description = des

  for var_name, dimension in nc_fid.dimensions.iteritems():
    w_nc_fid.createDimension(var_name, len(dimension) if not dimension.isunlimited() else None)

  for var_name, ncvar in nc_fid.variables.iteritems():

    outVar = w_nc_fid.createVariable(var_name, ncvar.datatype, ncvar.dimensions )
  
    ad = dict((k , ncvar.getncattr(k) ) for k in ncvar.ncattrs() )

    outVar.setncatts(  ad  )

    outVar[:] = ncvar[:]

  global_vars = dict((k , nc_fid.getncattr(k) ) for k in nc_fid.ncattrs() )
  
  for k in sorted(global_vars.keys()):
    w_nc_fid.setncattr(  k , global_vars[k]  )

  return w_nc_fid
# end copy
