import requests as rq

url_grib = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gdas.20211224/06/wave/gridded/gdaswave.t06z.arctic.9km.f000.grib2'

content_grib = rq.get(url_grib).content

print(f'size file: {(len(content_grib)/(1024**2)):.2f} MB')
with open('climate.grib2','wb') as file_grib:
	file_grib.write(content_grib)

print('sucess')
