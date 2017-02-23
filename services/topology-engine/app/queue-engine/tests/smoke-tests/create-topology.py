#!/usr/bin/python
from kafka import KafkaConsumer, KafkaProducer
import requests
import json

print "Clearing exiting topology."
headers = {'Content-Type': 'application/json'}
result_clear = requests.post('http://localhost:38080/cleanup', headers=headers)
print "Successful"

print "Creating new topology."
#data = {'controllers':[{'name': 'floodlight','host': 'kilda','port': 6653}],'links': [{'node1': 'sw1','node2': 'sw2'}],'switches': [{'name': 'sw1','dpid': '0000000000000001'},{'name': 'sw2','dpid': '0000000000000002'}]}
data = {
  'controllers': [
    {
      'host': '10.20.2.14',
      'name': 'floodlight',
      'port': 6653
    }
  ],
  'switches': [
    {
      'name': 's19',
      'dpid': 'SW0000001E08000843'
    },
    {
      'name': 's75',
      'dpid': 'SW0000B0D2F5C002BE'
    },
    {
      'name': 's79',
      'dpid': 'SW0000B0D2F5005D76'
    },
    {
      'name': 's47',
      'dpid': 'SW0000B0D2F5005DAC'
    },
    {
      'name': 's21',
      'dpid': 'SW0000B0D2F5C0046E'
    },
    {
      'name': 's29',
      'dpid': 'SW0000001E08000863'
    },
    {
      'name': 's28',
      'dpid': 'SW0000001E08000853'
    },
    {
      'name': 's27',
      'dpid': 'SW0000001E08000852'
    },
    {
     'name': 's88',
      'dpid': 'SW0000B0D2F5005B90'
    },
    {
      'name': 's87',
      'dpid': 'SW0000B0D2F5005AEE'
    },
    {
      'name': 's55',
      'dpid': 'SW00007072CFADBABE'
    },
    {
      'name': 's54',
      'dpid': 'SW0000B0D2F5005CD4'
    },
    {
      'name': 's85',
      'dpid': 'SW0000B0D2F5005AB8'
    },
    {
      'name': 's24',
      'dpid': 'SW0000B0D2F5B008B0'
    },
    {
      'name': 's84',
      'dpid': 'SW0000B0D2F5005B5A'
    },
    {
     'name': 's51',
      'dpid': 'SW0000B0D2F5005C32'
    },
    {
      'name': 's81',
      'dpid': 'SW0000B0D2F50059E0'
    },
    {
      'name': 's82',
      'dpid': 'SW0000B0D2F500527E'
    },
    {
      'name': 's49',
      'dpid': 'SW00007072CFABB56A'
    },
    {
      'name': 's22',
      'dpid': 'SW00007072CFADBB84'
    },
    {
      'name': 's80',
      'dpid': 'SW0000B0D2F5005BC6'
    },
    {
      'name': 's6',
      'dpid': 'SW0000B0D2F5005E18'
    },
    {
      'name': 's62',
      'dpid': 'SW0000B0D2F5B00104'
    },
    {
      'name': 's86',
      'dpid': 'SW00007072CFAA0F72'
    },
    {
      'name': 's5',
      'dpid': 'SW0000B0D2F5B0086E'
    },
    {
      'name': 's76',
      'dpid': 'SW0000B0D2F5005A82'
    },
    {
      'name': 's44',
      'dpid': 'SW0000B0D2F5B05145'
    },
    {
      'name': 's18',
      'dpid': 'SW00007072CFADB65C'
    },
    {
      'name': 's43',
      'dpid': 'SW0000B0D2F5B05104'
    },
    {
     'name': 's45',
      'dpid': 'SW00007072CFAA1458'
    },
    {
      'name': 's73',
      'dpid': 'SW0000B0D2F5005866'
    },
    {
      'name': 's50',
      'dpid': 'SW00007072CFADB9F8'
    },
    {
      'name': 's41',
      'dpid': 'SW0000B0D2F5015A16'
    },
    {
      'name': 's35',
      'dpid': 'SW00007072CFADC172'
    },
    {
      'name': 's66',
      'dpid': 'SW00007072CFAA1416'
    },
    {
      'name': 's33',
      'dpid': 'SW00007072CFADC238'
    },
    {
     'name': 's64',
      'dpid': 'SW00007072CFAA1206'
    },
    {
      'name': 's67',
      'dpid': 'SW00007072CFADB932'
    },
    {
      'name': 's37',
      'dpid': 'SW00007072CFABB35A'
    },
    {
      'name': 's69',
      'dpid': 'SW00007072CFABB6B4'
    },
    {
      'name': 's92',
      'dpid': 'SW00007072CFABBA0E'
    },
    {
      'name': 's36',
      'dpid': 'SW00007072CFADBF62'
    },
    {
      'name': 's77',
      'dpid': 'SW00007072CFAA1350'
    },
    {
     'name': 's58',
      'dpid': 'SW00007072CFADB974'
    },
    {
      'name': 's91',
      'dpid': 'SW00007072CFADBFA4'
    },
    {
      'name': 's11',
      'dpid': 'SW0000001E08000866'
    },
    {
      'name': 's59',
      'dpid': 'SW00007072CFD24974'
    },
    {
      'name': 's83',
      'dpid': 'SW00007072CFADB61A'
    },
    {
      'name': 's12',
      'dpid': 'SW0000001E08000893'
    },
    {
      'name': 's9',
      'dpid': 'SW0000001E080008A4'
    },
    {
      'name': 's13',
      'dpid': 'SW0000001E08000855'
    },
    {
      'name': 's78',
      'dpid': 'SW0000B0D2F5005A16'
    },
    {
      'name': 's8',
      'dpid': 'SW0000001E08000E45'
    },
    {
      'name': 's53',
      'dpid': 'SW0000B0D2F5005DE2'
    },
    {
      'name': 's23',
      'dpid': 'SW0000001E0800085C'
    },
    {
      'name': 's68',
      'dpid': 'SW0000B0D2F5005212'
    },
    {
      'name': 's7',
      'dpid': 'SW0000B0D2F5B00934'
    },
    {
      'name': 's46',
      'dpid': 'SW0000B0D2F5B05000'
    },
    {
      'name': 's20',
      'dpid': 'SW00007072CFADBFE6'
    },
    {
      'name': 's10',
      'dpid': 'SW0000001E08000DA2'
    },
    {
      'name': 's42',
      'dpid': 'SW0000B0D2F5005C9E'
    },
    {
      'name': 's74',
      'dpid': 'SW0000001E08000867'
    },
    {
      'name': 's65',
      'dpid': 'SW00007072CFADBDD6'
    },
    {
      'name': 's34',
      'dpid': 'SW00007072CFABB528'
    },
    {
     'name': 's1',
      'dpid': 'SW0000001E08000E2F'
    },
    {
      'name': 's2',
      'dpid': 'SW0000CC37AB32F318'
    },
    {
      'name': 's3',
      'dpid': 'SW0000CC37AB33020C'
    },
    {
      'name': 's17',
      'dpid': 'SW0000B0D2F5B0082C'
    },
    {
      'name': 's32',
      'dpid': 'SW00007072CF9F1C68'
    },
    {
      'name': 's63',
      'dpid': 'SW00007072CF9D5908'
    },
    {
      'name': 's26',
      'dpid': 'SW0000B0D2F5B00724'
    },
    {
     'name': 's48',
      'dpid': 'SW0000B0D2F5B007A8'
    },
    {
      'name': 's4',
      'dpid': 'SW0000B0D2F5B009FA'
    },
    {
      'name': 's89',
      'dpid': 'SW0000B0D2F5B004D3'
    },
    {
      'name': 's56',
      'dpid': 'SW0000B0D2F5C0057C'
    },
    {
      'name': 's57',
      'dpid': 'SW00007072CFADB596'
    },
    {
      'name': 's90',
      'dpid': 'SW00007072CFADB9B6'
    },
    {
      'name': 's25',
      'dpid': 'SW0000CC37AB3E741E'
    },
    {
     'name': 's52',
      'dpid': 'SW0000CC37AB3E7E6E'
    },
    {
      'name': 's71',
      'dpid': 'SW0000CC37AB32FCA2'
    },
    {
      'name': 's39',
      'dpid': 'SW0000CC37AB32F8C4'
    },
    {
      'name': 's15',
      'dpid': 'SW0000001E080010BE'
    },
    {
      'name': 's14',
      'dpid': 'SW0000001E08000F55'
    },
    {
      'name': 's70',
      'dpid': 'SW0000CC37AB3303DA'
    },
    {
      'name': 's38',
      'dpid': 'SW0000CC37AB32FDEC'
    },
    {
     'name': 's30',
      'dpid': 'SW0000001E08000F34'
    },
    {
      'name': 's93',
      'dpid': 'SW0000CC37AB32FD68'
    },
    {
      'name': 's60',
      'dpid': 'SW0000CC37AB330314'
    },
    {
      'name': 's31',
      'dpid': 'SW0000001E08001096'
    },
    {
      'name': 's94',
      'dpid': 'SW0000CC37AB330902'
    },
    {
      'name': 's61',
      'dpid': 'SW0000CC37AB32FDAA'
    },
    {
      'name': 's16',
      'dpid': 'SW0000001E080010FE'
    },
    {
     'name': 's72',
      'dpid': 'SW0000CC37AB32FC60'
    },
    {
      'name': 's40',
      'dpid': 'SW0000CC37AB3306B0'
    }
  ],
  'links': [
    {
      'node1': 's19',
      'node2': 's77'
    },
    {
      'node1': 's19',
      'node2': 's45'
    },
    {
      'node1': 's75',
      'node2': 's43'
    },
    {
      'node1': 's79',
      'node2': 's5'
    },
    {
      'node1': 's79',
      'node2': 's7'
    },
    {
      'node1': 's47',
      'node2': 's5'
    },
    {
      'node1': 's47',
      'node2': 's7'
    },
    {
      'node1': 's21',
      'node2': 's5'
    },
    {
      'node1': 's21',
      'node2': 's7'
    },
    {
      'node1': 's29',
      'node2': 's92'
    },
    {
      'node1': 's29',
      'node2': 's59'
    },
    {
      'node1': 's28',
      'node2': 's91'
    },
    {
      'node1': 's28',
      'node2': 's58'
    },
    {
      'node1': 's27',
      'node2': 's90'
    },
    {
      'node1': 's27',
      'node2': 's57'
    },
    {
      'node1': 's88',
      'node2': 's87'
    },
    {
      'node1': 's88',
      'node2': 's55'
    },
    {
      'node1': 's87',
      'node2': 's54'
    },
    {
      'node1': 's87',
      'node2': 's54'
    },
    {
      'node1': 's87',
      'node2': 's26'
    },
    {
      'node1': 's87',
      'node2': 's88'
    },
    {
      'node1': 's87',
      'node2': 's80'
    },
    {
      'node1': 's55',
      'node2': 's88'
    },
    {
      'node1': 's55',
      'node2': 's57'
    },
    {
      'node1': 's55',
      'node2': 's56'
    },
    {
      'node1': 's55',
      'node2': 's69'
    },
    {
      'node1': 's55',
      'node2': 's18'
    },
    {
      'node1': 's54',
      'node2': 's87'
    },
    {
      'node1': 's54',
      'node2': 's87'
    },
    {
      'node1': 's54',
      'node2': 's26'
    },
    {
      'node1': 's85',
      'node2': 's74'
    },
    {
      'node1': 's85',
      'node2': 's52'
    },
    {
      'node1': 's24',
      'node2': 's84'
    },
    {
      'node1': 's24',
      'node2': 's51'
    },
    {
      'node1': 's24',
      'node2': 's92'
    },
    {
      'node1': 's24',
      'node2': 's26'
    },
    {
      'node1': 's24',
      'node2': 's86'
    },
    {
      'node1': 's84',
      'node2': 's51'
    },
    {
      'node1': 's84',
      'node2': 's51'
    },
    {
      'node1': 's84',
      'node2': 's24'
    },
    {
      'node1': 's51',
      'node2': 's84'
    },
    {
      'node1': 's51',
      'node2': 's80'
    },
    {
      'node1': 's51',
      'node2': 's84'
    },
    {
      'node1': 's51',
      'node2': 's24'
    },
    {
      'node1': 's81',
      'node2': 's80'
    },
    {
      'node1': 's81',
      'node2': 's78'
    },
    {
      'node1': 's81',
      'node2': 's49'
    },
    {
      'node1': 's81',
      'node2': 's22'
    },
    {
      'node1': 's82',
      'node2': 's68'
    },
    {
      'node1': 's49',
      'node2': 's46'
    },
    {
      'node1': 's49',
      'node2': 's45'
    },
    {
      'node1': 's49',
      'node2': 's5'
    },
    {
      'node1': 's49',
      'node2': 's81'
    },
    {
      'node1': 's49',
      'node2': 's22'
    },
    {
      'node1': 's49',
      'node2': 's22'
    },
    {
      'node1': 's22',
      'node2': 's81'
    },
    {
      'node1': 's22',
      'node2': 's49'
    },
    {
      'node1': 's22',
      'node2': 's49'
    },
    {
      'node1': 's80',
      'node2': 's81'
    },
    {
      'node1': 's80',
      'node2': 's51'
    },
    {
      'node1': 's80',
      'node2': 's87'
    },
    {
      'node1': 's80',
      'node2': 's48'
    },
    {
      'node1': 's6',
      'node2': 's7'
    },
    {
      'node1': 's6',
      'node2': 's5'
    },
    {
      'node1': 's62',
      'node2': 's7'
    },
    {
      'node1': 's62',
      'node2': 's4'
    },
    {
      'node1': 's62',
      'node2': 's5'
    },
    {
      'node1': 's86',
      'node2': 's63'
    },
    {
      'node1': 's86',
      'node2': 's58'
    },
    {
      'node1': 's86',
      'node2': 's53'
    },
    {
      'node1': 's86',
      'node2': 's24'
    },
    {
      'node1': 's5',
      'node2': 's4'
    },
    {
      'node1': 's5',
      'node2': 's62'
    },
    {
      'node1': 's5',
      'node2': 's6'
    },
    {
      'node1': 's5',
      'node2': 's79'
    },
    {
      'node1': 's5',
      'node2': 's47'
    },
    {
      'node1': 's5',
      'node2': 's21'
    },
    {
      'node1': 's5',
      'node2': 's7'
    },
    {
      'node1': 's5',
      'node2': 's49'
    },
    {
      'node1': 's76',
      'node2': 's18'
    },
    {
      'node1': 's76',
      'node2': 's44'
    },
    {
      'node1': 's44',
      'node2': 's41'
    },
    {
      'node1': 's44',
      'node2': 's70'
    },
    {
      'node1': 's44',
      'node2': 's17'
    },
    {
      'node1': 's44',
      'node2': 's76'
    },
    {
      'node1': 's44',
      'node2': 's43'
    },
    {
      'node1': 's44',
      'node2': 's18'
    },
    {
      'node1': 's18',
      'node2': 's39'
    },
    {
      'node1': 's18',
      'node2': 's40'
    },
    {
      'node1': 's18',
      'node2': 's76'
    },
    {
      'node1': 's18',
      'node2': 's91'
    },
    {
      'node1': 's18',
      'node2': 's55'
    },
    {
      'node1': 's18',
      'node2': 's44'
    },
    {
      'node1': 's43',
      'node2': 's39'
    },
    {
      'node1': 's43',
      'node2': 's59'
    },
    {
      'node1': 's43',
      'node2': 's75'
    },
    {
      'node1': 's43',
      'node2': 's44'
    },
    {
      'node1': 's45',
      'node2': 's19'
    },
    {
      'node1': 's45',
      'node2': 's49'
    },
    {
      'node1': 's45',
      'node2': 's77'
    },
    {
      'node1': 's45',
      'node2': 's77'
    },
    {
      'node1': 's45',
      'node2': 's77'
    },
    {
      'node1': 's73',
      'node2': 's41'
    },
    {
      'node1': 's73',
      'node2': 's42'
    },
    {
      'node1': 's50',
      'node2': 's23'
    },
    {
      'node1': 's50',
      'node2': 's91'
    },
    {
      'node1': 's50',
      'node2': 's83'
    },
    {
      'node1': 's50',
      'node2': 's83'
    },
    {
      'node1': 's41',
      'node2': 's73'
    },
    {
      'node1': 's41',
      'node2': 's44'
    },
    {
      'node1': 's35',
      'node2': 's11'
    },
    {
      'node1': 's35',
      'node2': 's65'
    },
    {
      'node1': 's35',
      'node2': 's20'
    },
    {
      'node1': 's35',
      'node2': 's66'
    },
    {
      'node1': 's35',
      'node2': 's66'
    },
    {
      'node1': 's66',
      'node2': 's11'
    },
    {
      'node1': 's66',
      'node2': 's83'
    },
    {
      'node1': 's66',
      'node2': 's67'
    },
    {
      'node1': 's66',
      'node2': 's35'
    },
    {
      'node1': 's66',
      'node2': 's35'
    },
    {
      'node1': 's33',
      'node2': 's36'
    },
    {
      'node1': 's33',
      'node2': 's9'
    },
    {
      'node1': 's33',
      'node2': 's83'
    },
    {
      'node1': 's33',
      'node2': 's64'
    },
    {
      'node1': 's33',
      'node2': 's64'
    },
    {
      'node1': 's64',
      'node2': 's9'
    },
    {
      'node1': 's64',
      'node2': 's53'
    },
    {
      'node1': 's64',
      'node2': 's33'
    },
    {
      'node1': 's64',
      'node2': 's33'
    },
    {
      'node1': 's67',
      'node2': 's12'
    },
    {
      'node1': 's67',
      'node2': 's34'
    },
    {
      'node1': 's67',
      'node2': 's66'
    },
    {
      'node1': 's67',
      'node2': 's36'
    },
    {
      'node1': 's67',
      'node2': 's36'
    },
    {
      'node1': 's37',
      'node2': 's13'
    },
    {
      'node1': 's37',
      'node2': 's92'
    },
    {
      'node1': 's37',
      'node2': 's69'
    },
    {
      'node1': 's69',
      'node2': 's13'
    },
    {
      'node1': 's69',
      'node2': 's55'
    },
    {
      'node1': 's69',
      'node2': 's37'
    },
    {
      'node1': 's92',
      'node2': 's29'
    },
    {
      'node1': 's92',
      'node2': 's24'
    },
    {
      'node1': 's92',
      'node2': 's37'
    },
    {
      'node1': 's92',
      'node2': 's59'
    },
    {
      'node1': 's92',
      'node2': 's59'
    },
    {
      'node1': 's36',
      'node2': 's12'
    },
    {
      'node1': 's36',
      'node2': 's33'
    },
    {
      'node1': 's36',
      'node2': 's67'
    },
    {
      'node1': 's36',
      'node2': 's67'
    },
    {
      'node1': 's77',
      'node2': 's19'
    },
    {
      'node1': 's77',
      'node2': 's46'
    },
    {
      'node1': 's77',
      'node2': 's45'
    },
    {
      'node1': 's77',
      'node2': 's45'
    },
    {
      'node1': 's77',
      'node2': 's45'
    },
    {
      'node1': 's58',
      'node2': 's28'
    },
    {
      'node1': 's58',
      'node2': 's32'
    },
    {
      'node1': 's58',
      'node2': 's86'
    },
    {
      'node1': 's58',
      'node2': 's91'
    },
    {
      'node1': 's58',
      'node2': 's91'
    },
    {
      'node1': 's91',
      'node2': 's28'
    },
    {
      'node1': 's91',
      'node2': 's18'
    },
    {
      'node1': 's91',
      'node2': 's50'
    },
    {
      'node1': 's91',
      'node2': 's58'
    },
    {
      'node1': 's91',
      'node2': 's58'
    },
    {
      'node1': 's11',
      'node2': 's66'
    },
    {
      'node1': 's11',
      'node2': 's35'
    },
    {
      'node1': 's59',
      'node2': 's29'
    },
    {
      'node1': 's59',
      'node2': 's43'
    },
    {
      'node1': 's59',
      'node2': 's92'
    },
    {
      'node1': 's59',
      'node2': 's92'
    },
    {
      'node1': 's83',
      'node2': 's23'
    },
    {
      'node1': 's83',
      'node2': 's66'
    },
    {
      'node1': 's83',
      'node2': 's33'
    },
    {
      'node1': 's83',
      'node2': 's50'
    },
    {
      'node1': 's83',
      'node2': 's50'
    },
    {
      'node1': 's12',
      'node2': 's67'
    },
    {
      'node1': 's12',
      'node2': 's36'
    },
    {
      'node1': 's9',
      'node2': 's64'
    },
    {
      'node1': 's9',
      'node2': 's33'
    },
    {
      'node1': 's13',
      'node2': 's69'
    },
    {
      'node1': 's13',
      'node2': 's37'
    },
    {
      'node1': 's78',
      'node2': 's46'
    },
    {
      'node1': 's78',
      'node2': 's81'
    },
    {
      'node1': 's78',
      'node2': 's20'
    },
    {
      'node1': 's8',
      'node2': 's63'
    },
    {
      'node1': 's8',
      'node2': 's32'
    },
    {
      'node1': 's53',
      'node2': 's64'
    },
    {
      'node1': 's53',
      'node2': 's86'
    },
    {
      'node1': 's23',
      'node2': 's83'
    },
    {
      'node1': 's23',
      'node2': 's50'
    },
    {
      'node1': 's68',
      'node2': 's82'
    },
    {
      'node1': 's7',
      'node2': 's62'
    },
    {
      'node1': 's7',
      'node2': 's4'
    },
    {
      'node1': 's7',
      'node2': 's79'
    },
    {
      'node1': 's7',
      'node2': 's47'
    },
    {
      'node1': 's7',
      'node2': 's21'
    },
    {
      'node1': 's7',
      'node2': 's6'
    },
    {
      'node1': 's7',
      'node2': 's5'
    },
    {
      'node1': 's7',
      'node2': 's46'
    },
    {
      'node1': 's7',
      'node2': 's48'
    },
    {
      'node1': 's46',
      'node2': 's77'
    },
    {
      'node1': 's46',
      'node2': 's49'
    },
    {
      'node1': 's46',
      'node2': 's7'
    },
    {
      'node1': 's46',
      'node2': 's78'
    },
    {
      'node1': 's46',
      'node2': 's20'
    },
    {
      'node1': 's20',
      'node2': 's78'
    },
    {
      'node1': 's20',
      'node2': 's35'
    },
    {
      'node1': 's20',
      'node2': 's46'
    },
    {
      'node1': 's10',
      'node2': 's65'
    },
    {
      'node1': 's10',
      'node2': 's34'
    },
    {
      'node1': 's42',
      'node2': 's74'
    },
    {
      'node1': 's42',
      'node2': 's73'
    },
    {
      'node1': 's42',
      'node2': 's17'
    },
    {
      'node1': 's74',
      'node2': 's85'
    },
    {
      'node1': 's74',
      'node2': 's42'
    },
    {
      'node1': 's74',
      'node2': 's17'
    },
    {
      'node1': 's65',
      'node2': 's10'
    },
    {
      'node1': 's65',
      'node2': 's35'
    },
    {
      'node1': 's65',
      'node2': 's34'
    },
    {
      'node1': 's65',
      'node2': 's34'
    },
    {
      'node1': 's34',
      'node2': 's10'
    },
    {
      'node1': 's34',
      'node2': 's67'
    },
    {
      'node1': 's34',
      'node2': 's65'
    },
    {
      'node1': 's34',
      'node2': 's65'
    },
    {
      'node1': 's1',
      'node2': 's3'
    },
    {
      'node1': 's1',
      'node2': 's2'
    },
    {
      'node1': 's2',
      'node2': 's1'
    },
    {
      'node1': 's2',
      'node2': 's3'
    },
    {
      'node1': 's2',
      'node2': 's3'
    },
    {
      'node1': 's3',
      'node2': 's1'
    },
    {
      'node1': 's3',
      'node2': 's26'
    },
    {
      'node1': 's3',
      'node2': 's2'
    },
    {
      'node1': 's3',
      'node2': 's2'
    },
    {
      'node1': 's17',
      'node2': 's44'
    },
    {
      'node1': 's17',
      'node2': 's74'
    },
    {
      'node1': 's17',
      'node2': 's42'
    },
    {
      'node1': 's17',
      'node2': 's25'
    },
    {
      'node1': 's17',
      'node2': 's52'
    },
    {
      'node1': 's32',
      'node2': 's8'
    },
    {
      'node1': 's32',
      'node2': 's58'
    },
    {
      'node1': 's32',
      'node2': 's63'
    },
    {
      'node1': 's32',
      'node2': 's63'
    },
    {
      'node1': 's63',
      'node2': 's8'
    },
    {
      'node1': 's63',
      'node2': 's86'
    },
    {
      'node1': 's63',
      'node2': 's32'
    },
    {
      'node1': 's63',
      'node2': 's32'
    },
    {
      'node1': 's26',
      'node2': 's54'
    },
    {
      'node1': 's26',
      'node2': 's89'
    },
    {
      'node1': 's26',
      'node2': 's3'
    },
    {
      'node1': 's26',
      'node2': 's48'
    },
    {
      'node1': 's26',
      'node2': 's87'
    },
    {
      'node1': 's26',
      'node2': 's24'
    },
    {
      'node1': 's48',
      'node2': 's26'
    },
    {
      'node1': 's48',
      'node2': 's80'
    },
    {
      'node1': 's48',
      'node2': 's7'
    },
    {
      'node1': 's4',
      'node2': 's5'
    },
    {
      'node1': 's4',
      'node2': 's62'
    },
    {
      'node1': 's4',
      'node2': 's7'
    },
    {
      'node1': 's89',
      'node2': 's90'
    },
    {
      'node1': 's89',
      'node2': 's56'
    },
    {
      'node1': 's89',
      'node2': 's26'
    },
    {
      'node1': 's56',
      'node2': 's55'
    },
    {
      'node1': 's56',
      'node2': 's89'
    },
    {
      'node1': 's57',
      'node2': 's55'
    },
    {
      'node1': 's57',
      'node2': 's27'
    },
    {
      'node1': 's57',
      'node2': 's90'
    },
    {
      'node1': 's90',
      'node2': 's27'
    },
    {
      'node1': 's90',
      'node2': 's89'
    },
    {
      'node1': 's90',
      'node2': 's57'
    },
    {
      'node1': 's25',
      'node2': 's40'
    },
    {
      'node1': 's25',
      'node2': 's40'
    },
    {
      'node1': 's25',
      'node2': 's94'
    },
    {
      'node1': 's25',
      'node2': 's17'
    },
    {
      'node1': 's25',
      'node2': 's52'
    },
    {
      'node1': 's25',
      'node2': 's52'
    },
    {
      'node1': 's52',
      'node2': 's72'
    },
    {
      'node1': 's52',
      'node2': 's72'
    },
    {
      'node1': 's52',
      'node2': 's61'
    },
    {
      'node1': 's52',
      'node2': 's17'
    },
    {
      'node1': 's52',
      'node2': 's85'
    },
    {
      'node1': 's52',
      'node2': 's25'
    },
    {
      'node1': 's52',
      'node2': 's25'
    },
    {
      'node1': 's71',
      'node2': 's15'
    },
    {
      'node1': 's71',
      'node2': 's72'
    },
    {
      'node1': 's71',
      'node2': 's39'
    },
    {
      'node1': 's71',
      'node2': 's39'
    },
    {
      'node1': 's39',
      'node2': 's15'
    },
    {
      'node1': 's39',
      'node2': 's40'
    },
    {
      'node1': 's39',
      'node2': 's18'
    },
    {
      'node1': 's39',
      'node2': 's43'
    },
    {
      'node1': 's39',
      'node2': 's71'
    },
    {
      'node1': 's39',
      'node2': 's71'
    },
    {
      'node1': 's15',
      'node2': 's71'
    },
    {
      'node1': 's15',
      'node2': 's39'
    },
    {
      'node1': 's14',
      'node2': 's70'
    },
    {
      'node1': 's14',
      'node2': 's38'
    },
    {
      'node1': 's70',
      'node2': 's44'
    },
    {
      'node1': 's70',
      'node2': 's14'
    },
    {
      'node1': 's70',
      'node2': 's72'
    },
    {
      'node1': 's70',
      'node2': 's38'
    },
    {
      'node1': 's70',
      'node2': 's38'
    },
    {
      'node1': 's38',
      'node2': 's14'
    },
    {
      'node1': 's38',
      'node2': 's40'
    },
    {
      'node1': 's38',
      'node2': 's70'
    },
    {
      'node1': 's38',
      'node2': 's70'
    },
    {
      'node1': 's30',
      'node2': 's93'
    },
    {
      'node1': 's30',
      'node2': 's60'
    },
    {
      'node1': 's93',
      'node2': 's30'
    },
    {
      'node1': 's93',
      'node2': 's94'
    },
    {
      'node1': 's93',
      'node2': 's60'
    },
    {
      'node1': 's93',
      'node2': 's60'
    },
    {
      'node1': 's60',
      'node2': 's30'
    },
    {
      'node1': 's60',
      'node2': 's61'
    },
    {
      'node1': 's60',
      'node2': 's93'
    },
    {
      'node1': 's60',
      'node2': 's93'
    },
    {
      'node1': 's31',
      'node2': 's94'
    },
    {
      'node1': 's31',
      'node2': 's61'
    },
    {
      'node1': 's94',
      'node2': 's31'
    },
    {
      'node1': 's94',
      'node2': 's25'
    },
    {
      'node1': 's94',
      'node2': 's93'
    },
    {
      'node1': 's94',
      'node2': 's61'
    },
    {
      'node1': 's94',
      'node2': 's61'
    },
    {
      'node1': 's61',
      'node2': 's31'
    },
    {
      'node1': 's61',
      'node2': 's52'
    },
    {
      'node1': 's61',
      'node2': 's60'
    },
    {
      'node1': 's61',
      'node2': 's94'
    },
    {
      'node1': 's61',
      'node2': 's94'
    },
    {
      'node1': 's16',
      'node2': 's72'
    },
    {
      'node1': 's16',
      'node2': 's40'
    },
    {
      'node1': 's72',
      'node2': 's16'
    },
    {
      'node1': 's72',
      'node2': 's71'
    },
    {
      'node1': 's72',
      'node2': 's70'
    },
    {
      'node1': 's72',
      'node2': 's52'
    },
    {
      'node1': 's72',
      'node2': 's52'
    },
    {
      'node1': 's72',
      'node2': 's40'
    },
    {
      'node1': 's72',
      'node2': 's40'
    },
    {
      'node1': 's40',
      'node2': 's16'
    },
    {
      'node1': 's40',
      'node2': 's39'
    },
    {
      'node1': 's40',
      'node2': 's18'
    },
    {
      'node1': 's40',
      'node2': 's38'
    },
    {
      'node1': 's40',
      'node2': 's25'
    },
    {
      'node1': 's40',
      'node2': 's25'
    },
    {
      'node1': 's40',
      'node2': 's72'
    },
    {
      'node1': 's40',
      'node2': 's72'
    }
  ]
}

j_data = json.dumps(data)
result_switches = requests.post('http://localhost:38080/topology', data=j_data, headers=headers)
print result_switches.text
print "Successful"


