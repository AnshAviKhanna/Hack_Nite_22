import discord
from math import *

from requests import get
def get_data(city_1,city_2):
    '''
    d={'mumbai':{"place_id":284925074,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7888990,"boundingbox":["18.8939566","19.2694771","72.776333","72.9817485"],"lat":"19.0759899","lon":"72.8773928","display_name":"Mumbai, Mumbai Metropolitan Region, Mumbai Suburban, Maharashtra, India","class":"boundary","type":"administrative","importance":0.7599499101971479,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
    'bangalore':{"place_id":285917408,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7902476,"boundingbox":["12.8340125","13.1436649","77.4601025","77.7840515"],"lat":"12.9767936","lon":"77.590082","display_name":"Bengaluru, Bangalore North, Bangalore Urban, Karnataka, India","class":"boundary","type":"administrative","importance":0.7094348238975636,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
    'lucknow':{"place_id":446776,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":245753718,"boundingbox":["26.6781","26.9981","80.7746001","81.0946001"],"lat":"26.8381","lon":"80.9346001","display_name":"Lucknow, Sadar, Lucknow, Uttar Pradesh, 226019, India","class":"place","type":"city","importance":0.6902147473320663,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},
    'chennai':{"place_id":41572401,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":3233393892,"boundingbox":["12.9236939","13.2436939","80.110186","80.430186"],"lat":"13.0836939","lon":"80.270186","display_name":"Chennai, Chennai District, Tamil Nadu, 600001, India","class":"place","type":"city","importance":0.7280422595919259,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},
    'delhi':{"place_id":24970445,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":2702400314,"boundingbox":["28.4917178","28.8117178","77.0619388","77.3819388"],"lat":"28.6517178","lon":"77.2219388","display_name":"Delhi, Kotwali Tehsil, Central Delhi, Delhi, 110006, India","class":"place","type":"city","importance":0.7602894986544559,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},{"place_id":284307506,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":128565,"boundingbox":["42.4230572","42.4376091","-91.3406123","-91.3208259"],"lat":"42.4297057","lon":"-91.3309112","display_name":"Delhi, Delaware County, Iowa, United States","class":"boundary","type":"administrative","importance":0.5331649175308649,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284508695,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":137528,"boundingbox":["44.592216","44.60357","-95.223451","-95.203144"],"lat":"44.5991256","lon":"-95.211113","display_name":"Delhi, Redwood County, Minnesota, United States","class":"boundary","type":"administrative","importance":0.5293327847381092,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284645003,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":176126,"boundingbox":["42.256461","42.297427","-74.938181","-74.894297"],"lat":"42.2781401","lon":"-74.9159946","display_name":"Village of Delhi, Town of Delhi, Delaware County, New York, United States","class":"boundary","type":"administrative","importance":0.5106648553911631,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284593701,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":3301392,"boundingbox":["42.198785","42.350216","-75.039541","-74.791888"],"lat":"42.2781401","lon":"-74.9159946","display_name":"Town of Delhi, Delaware County, New York, 13753, United States","class":"boundary","type":"administrative","importance":0.5016086140508969,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":965846,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":300479055,"boundingbox":["42.8144957","42.8944957","-80.5383709","-80.4583709"],"lat":"42.8544957","lon":"-80.4983709","display_name":"Delhi, Norfolk County, Southwestern Ontario, Ontario, N4B 2K6, Canada","class":"place","type":"town","importance":0.41162856080067534,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_town.p.20.png"},{"place_id":284328194,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":4489246,"boundingbox":["36.8913167","38.8868198","95.7173536","98.1479422"],"lat":"37.3690819","lon":"97.36011","display_name":"Delingha City, Haixi Mongol and Tibetan Autonomous Prefecture, Qinghai, China","class":"boundary","type":"administrative","importance":0.4004118308283028,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":286204426,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":12074535,"boundingbox":["33.708633","33.7224594","-117.8680358","-117.8565061"],"lat":"33.7160692","lon":"-117.862108","display_name":"Delhi, Santa Ana, Orange County, California, United States","class":"boundary","type":"administrative","importance":0.4,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":283229980,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":132164,"boundingbox":["32.434949","32.471221","-91.506983","-91.471765"],"lat":"32.4576421","lon":"-91.4931736","display_name":"Delhi, Richland Parish, Louisiana, United States","class":"boundary","type":"administrative","importance":0.39999782720980437,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":172419,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":151635021,"boundingbox":["37.6221559","37.6621559","-104.037137","-103.997137"],"lat":"37.6421559","lon":"-104.017137","display_name":"Delhi, Las Animas County, Colorado, United States","class":"place","type":"hamlet","importance":0.3885709817044999,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},
    'paris':{"place_id":283551335,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7444,"boundingbox":["48.8155755","48.902156","2.224122","2.4697602"],"lat":"48.8588897","lon":"2.3200410217200766","display_name":"Paris, Ile-de-France, Metropolitan France, France","class":"boundary","type":"administrative","importance":0.9317101715588673,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285714751,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":17807753,"boundingbox":["48.6934951","49.0134951","2.1883915","2.5083915"],"lat":"48.8534951","lon":"2.3483915","display_name":"Paris, Ile-de-France, Metropolitan France, 75000, France","class":"place","type":"city","importance":0.9317101715588673,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},{"place_id":284895425,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":115357,"boundingbox":["33.6206345","33.7383866","-95.6279396","-95.4354115"],"lat":"33.6617962","lon":"-95.555513","display_name":"Paris, Lamar County, Texas, 75460, United States","class":"boundary","type":"administrative","importance":0.5961645097134651,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284766358,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":130722,"boundingbox":["38.164922","38.238271","-84.307326","-84.232089"],"lat":"38.2097987","lon":"-84.2529869","display_name":"Paris, Bourbon County, Kentucky, United States","class":"boundary","type":"administrative","importance":0.5486843760767399,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285167020,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":1641193,"boundingbox":["48.8155755","48.902156","2.224122","2.4697602"],"lat":"48.8588897","lon":"2.3200410217200766","display_name":"Paris, Ile-de-France, Metropolitan France, France","class":"boundary","type":"administrative","importance":0.5283953917728152,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":202933,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":153536155,"boundingbox":["36.2619461","36.3419461","-88.3658578","-88.2858578"],"lat":"36.3019461","lon":"-88.3258578","display_name":"Paris, Henry County, Tennessee, 38242, United States","class":"place","type":"town","importance":0.5150690427980547,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_town.p.20.png"},{"place_id":283838598,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":197171,"boundingbox":["36.266003","36.329016","-88.367113","-88.265067"],"lat":"36.29755","lon":"-88.31007912277815","display_name":"Paris, Henry County, Tennessee, 38242, United States","class":"boundary","type":"administrative","importance":0.5150690427980547,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":181957,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":153467139,"boundingbox":["39.571146","39.651146","-87.7361374","-87.6561374"],"lat":"39.611146","lon":"-87.6961374","display_name":"Paris, Edgar County, Illinois, 61944, United States","class":"place","type":"town","importance":0.5144799592274194,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_town.p.20.png"},{"place_id":283923341,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":126166,"boundingbox":["39.581493","39.649981","-87.721046","-87.649203"],"lat":"39.6157435","lon":"-87.69408996387567","display_name":"Paris, Edgar County, Illinois, 61944, United States","class":"boundary","type":"administrative","importance":0.5144799592274194,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":286134367,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":12165996,"boundingbox":["44.1754185","44.3124081","-70.566213","-70.414966"],"lat":"44.259954","lon":"-70.500641","display_name":"Paris, Oxford County, Maine, 04281, United States","class":"boundary","type":"administrative","importance":0.5090701377223524,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
    'london':{"place_id":285639790,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":107775,"boundingbox":["51.3473219","51.6673219","-0.2876474","0.0323526"],"lat":"51.5073219","lon":"-0.1276474","display_name":"London, Greater London, England, SW1A 2DX, United Kingdom","class":"place","type":"city","importance":0.9307827616237295,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},{"place_id":332008866,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":65606,"boundingbox":["51.2867601","51.6918741","-0.5103751","0.3340155"],"lat":"51.4893335","lon":"-0.14405508452768728","display_name":"London, Greater London, England, United Kingdom","class":"boundary","type":"administrative","importance":0.9307827616237295,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":283161129,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":51800,"boundingbox":["51.5068696","51.5233122","-0.1138211","-0.0727493"],"lat":"51.5156177","lon":"-0.0919983","display_name":"City of London, Greater London, England, United Kingdom","class":"boundary","type":"administrative","importance":0.6865111547516773,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285154359,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7485368,"boundingbox":["42.8245667","43.0730461","-81.3906556","-81.1070784"],"lat":"42.9832406","lon":"-81.243372","display_name":"London, Southwestern Ontario, Ontario, Canada","class":"boundary","type":"administrative","importance":0.6659177286656098,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284942967,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":130591,"boundingbox":["37.079759","37.15226","-84.126262","-84.035957"],"lat":"37.1289771","lon":"-84.0832646","display_name":"London, Laurel County, Kentucky, 40741, United States","class":"boundary","type":"administrative","importance":0.5412922449371916,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284413180,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":182481,"boundingbox":["39.85928","39.921786","-83.478923","-83.389997"],"lat":"39.8864493","lon":"-83.448253","display_name":"London, Madison County, Ohio, 43140, United States","class":"boundary","type":"administrative","importance":0.5050655424601236,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":284312214,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":111457,"boundingbox":["35.3169503","35.3389327","-93.2716305","-93.1874567"],"lat":"35.328973","lon":"-93.2529553","display_name":"London, Pope County, Arkansas, 7, United States","class":"boundary","type":"administrative","importance":0.49823578717763006,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":283948058,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":2730965,"boundingbox":["36.4734452","36.4884367","-119.4497699","-119.4385395"],"lat":"36.4760619","lon":"-119.4431785","display_name":"London, Tulare County, California, United States","class":"place","type":"village","importance":0.47680090174386036,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":231295,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":154301303,"boundingbox":["38.1743567","38.2143567","-81.3886944","-81.3486944"],"lat":"38.1943567","lon":"-81.3686944","display_name":"London, Kanawha County, West Virginia, 25126, United States","class":"place","type":"hamlet","importance":0.44224222283715364,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":2962345,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":385732547,"boundingbox":["63.6620113","63.7020113","22.6923784","22.7323784"],"lat":"63.6820113","lon":"22.7123784","display_name":"London, Jakobstad, Jakobstadsregionen, Ostrobothnia, Western and Central Finland, Mainland Finland, 68600, Finland","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},
    'chicago':{"place_id":284945561,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":122604,"boundingbox":["41.644531","42.0230396","-87.940101","-87.5240812"],"lat":"41.8755616","lon":"-87.6244212","display_name":"Chicago, Cook County, Illinois, United States","class":"boundary","type":"administrative","importance":0.8515295727100248,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":61275606,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":5545539561,"boundingbox":["-33.73745","-33.69745","18.9763167","19.0163167"],"lat":"-33.71745","lon":"18.9963167","display_name":"Chicago, Drakenstein Ward 24, Paarl, Drakenstein Local Municipality, Cape Winelands District Municipality, Western Cape, 7646, South Africa","class":"place","type":"suburb","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":84311436,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":8327507255,"boundingbox":["-18.9735788","-18.9335788","29.7753081","29.8153081"],"lat":"-18.9535788","lon":"29.7953081","display_name":"Chicago, Kwekwe, Midlands Province, Zimbabwe","class":"place","type":"suburb","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":9598254,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":1028802194,"boundingbox":["4.9224371","4.9424371","-52.341324","-52.321324"],"lat":"4.9324371","lon":"-52.331324","display_name":"Chicago, Cayenne, Arrondissement de Cayenne, French Guiana, 97300, France","class":"place","type":"neighbourhood","importance":0.35},{"place_id":41081398,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":3201711331,"boundingbox":["18.4072472","18.4272472","-68.9856563","-68.9656563"],"lat":"18.4172472","lon":"-68.9756563","display_name":"Chicago, La Romana, 2200, Dominican Republic","class":"place","type":"neighbourhood","importance":0.35},{"place_id":23230967,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":2527011332,"boundingbox":["13.376","13.416","121.0784","121.1184"],"lat":"13.396","lon":"121.0984","display_name":"Chicago, Lumangbayan, Oriental Mindoro, Mimaropa, Philippines","class":"place","type":"hamlet","importance":0.35,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":20218732,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":2285155351,"boundingbox":["17.7949465","17.8349465","-88.3315477","-88.2915477"],"lat":"17.8149465","lon":"-88.3115477","display_name":"Chicago, Belize District, Belize","class":"place","type":"hamlet","importance":0.35,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},
    'kolkata':{"place_id":286008146,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":9381363,"boundingbox":["22.4503235","22.6325362","88.2406237","88.4589549"],"lat":"22.5726723","lon":"88.3638815","display_name":"Kolkata, West Bengal, India","class":"boundary","type":"administrative","importance":0.7340385346278306,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
    'jaipur':{"place_id":1115915,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":315734346,"boundingbox":["26.7554576","27.0754576","75.6589817","75.9789817"],"lat":"26.9154576","lon":"75.8189817","display_name":"Jaipur, Jaipur Municipal Corporation, Jaipur Tehsil, Jaipur, Rajasthan, 302001, India","class":"place","type":"city","importance":0.6583812955126459,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},{"place_id":46526259,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":3998324333,"boundingbox":["23.3970993","23.4370993","86.1243853","86.1643853"],"lat":"23.4170993","lon":"86.1443853","display_name":"Jaipur, Puruliya, West Bengal, 723201, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":95430746,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":9287892031,"boundingbox":["23.3933443","23.4333443","85.2796218","85.3196218"],"lat":"23.4133443","lon":"85.2996218","display_name":"Jaipur, Ranchi, Kanke, Ranchi, Jharkhand, 834008, India","class":"place","type":"suburb","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":80973177,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":7936530808,"boundingbox":["29.1029234","29.1429234","79.6668848","79.7068848"],"lat":"29.1229234","lon":"79.6868848","display_name":"Jaipur, Lalkuan, Nainital, Uttarakhand, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":203448701,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"way","osm_id":444459469,"boundingbox":["20.7638266","20.7664572","78.7350892","78.7409923"],"lat":"20.7651115","lon":"78.73839817829418","display_name":"Jaipur, Seloo, Wardha, Maharashtra, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":63008880,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":5837060090,"boundingbox":["19.8616631","19.9016631","76.7534265","76.7934265"],"lat":"19.8816631","lon":"76.7734265","display_name":"Jaipur, Sengaon, Hingoli, Maharashtra, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":46433465,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":3957021160,"boundingbox":["20.6631842","20.7031842","76.2610542","76.3010542"],"lat":"20.6831842","lon":"76.2810542","display_name":"Jaipur, Motala, Buldhana, Maharashtra, 443103, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":76818493,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":7152036488,"boundingbox":["22.5705564","22.6105564","87.9114803","87.9514803"],"lat":"22.5905564","lon":"87.9314803","display_name":"Jaipur, Amta - II, Howrah, West Bengal, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":332985515,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":9579447782,"boundingbox":["24.8747851","24.9147851","79.4720474","79.5120474"],"lat":"24.8947851","lon":"79.4920474","display_name":"Jaipur, Chhatarpur Tahsil, Chhatarpur, Madhya Pradesh, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":66812338,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":6221036201,"boundingbox":["24.5660172","24.6060172","86.8247351","86.8647351"],"lat":"24.5860172","lon":"86.8447351","display_name":"Jaipur, Katoria, Banka, Bihar, India","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},
    'sydney':{"place_id":286064526,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":13766899,"boundingbox":["-34.0298439","-33.7098439","151.0482848","151.3682848"],"lat":"-33.8698439","lon":"151.2082848","display_name":"Sydney, Council of the City of Sydney, New South Wales, 2000, Australia","class":"place","type":"city","importance":0.8245908962989684,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},{"place_id":324802023,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":5750005,"boundingbox":["-34.1732416","-33.3641864","150.260825","151.343898"],"lat":"-33.768528","lon":"150.9568559523945","display_name":"Sydney, Blacktown City Council, New South Wales, Australia","class":"boundary","type":"administrative","importance":0.8245908962989684,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285927122,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":9132453,"boundingbox":["46.1071148","46.1786423","-60.2161333","-60.1450518"],"lat":"46.137977","lon":"-60.194092","display_name":"Sydney, Cape Breton Regional Municipality, Cape Breton County, Nova Scotia, Canada","class":"boundary","type":"administrative","importance":0.5658173637393935,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285443191,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":5729534,"boundingbox":["-33.8797755","-33.8561096","151.1970047","151.223011"],"lat":"-33.8681512","lon":"151.21014511728356","display_name":"Sydney, Council of the City of Sydney, New South Wales, 2000, Australia","class":"boundary","type":"administrative","importance":0.5648447123160637,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":285181322,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":1251066,"boundingbox":["-33.9243832","-33.8535199","151.1748953","151.2330104"],"lat":"-33.8888621","lon":"151.2048978618509","display_name":"Council of the City of Sydney, New South Wales, Australia","class":"boundary","type":"administrative","importance":0.5602672043141234,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},{"place_id":199343762,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"way","osm_id":434309411,"boundingbox":["-33.8794356","-33.8775558","151.20339","151.2048011"],"lat":"-33.87849425","lon":"151.2040733935","display_name":"Chinatown, Haymarket, Sydney, Council of the City of Sydney, New South Wales, 2000, Australia","class":"place","type":"neighbourhood","importance":0.48265030002841014},{"place_id":218380,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":154086316,"boundingbox":["27.9433563","27.9833563","-82.2273118","-82.1873118"],"lat":"27.9633563","lon":"-82.2073118","display_name":"Sydney, Hillsborough County, Florida, 33527, United States","class":"place","type":"hamlet","importance":0.3970855185391935,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"},{"place_id":169355,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":151536369,"boundingbox":["46.7108155","46.7508155","-98.7898262","-98.7498262"],"lat":"46.7308155","lon":"-98.7698262","display_name":"Sydney, Stutsman County, North Dakota, United States","class":"place","type":"village","importance":0.375,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_village.p.20.png"}}
'''
    d={'mumbai':{"place_id":284925074,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7888990,"boundingbox":["18.8939566","19.2694771","72.776333","72.9817485"],"lat":"19.0759899","lon":"72.8773928","display_name":"Mumbai, Mumbai Metropolitan Region, Mumbai Suburban, Maharashtra, India","class":"boundary","type":"administrative","importance":0.7599499101971479,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
'bangalore':{"place_id":285917408,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"relation","osm_id":7902476,"boundingbox":["12.8340125","13.1436649","77.4601025","77.7840515"],"lat":"12.9767936","lon":"77.590082","display_name":"Bengaluru, Bangalore North, Bangalore Urban, Karnataka, India","class":"boundary","type":"administrative","importance":0.7094348238975636,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png"},
'lucknow':{"place_id":446776,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":245753718,"boundingbox":["26.6781","26.9981","80.7746001","81.0946001"],"lat":"26.8381","lon":"80.9346001","display_name":"Lucknow, Sadar, Lucknow, Uttar Pradesh, 226019, India","class":"place","type":"city","importance":0.6902147473320663,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"},
'chennai':{"place_id":41572401,"licence":"Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright","osm_type":"node","osm_id":3233393892,"boundingbox":["12.9236939","13.2436939","80.110186","80.430186"],"lat":"13.0836939","lon":"80.270186","display_name":"Chennai, Chennai District, Tamil Nadu, 600001, India","class":"place","type":"city","importance":0.7280422595919259,"icon":"https://nominatim.openstreetmap.org/ui/mapicons//poi_place_city.p.20.png"}}
    lat_1=float(d[city_1]['lat'])/57.29577951
    lat_2=float(d[city_2]['lat'])/57.29577951
    lon_1=float(d[city_1]['lon'])/57.29577951
    lon_2=float(d[city_2]['lon'])/57.29577951
    distance= 3963.0 * acos((sin(lat_1) * sin(lat_2)) + cos(lat_1) * cos(lat_2) * cos(lon_2 - lon_1))*1.609344
    message=discord.Embed(title=f'{city_1.upper()} to {city_2.upper()}',color=0xFF7F24)
    message.add_field(name='Distance',value=f'{distance:.2f} km',inline=False)
    message.add_field(name='Time (Low Traffic)',value=f"{distance/80:.2f} hours",inline=False)
    return message