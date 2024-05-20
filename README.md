# python-test

Reads the CSV file of IP traffic for each device. Then adds the input and out of each device and total traffic of all devices. 

[{'device': 'r1', 'input': 0, 'intf': 'et1', 'output': '110'},
 {'device': 'r1', 'input': '102', 'intf': 'et2', 'output': '112'},
 {'device': 'r1', 'input': '103', 'intf': 'et3', 'output': '113'},
 {'device': 'r2', 'input': '200', 'intf': 'et1', 'output': '210'},
 {'device': 'r2', 'input': '202', 'intf': 'et2', 'output': '212'},
 {'device': 'r2', 'input': '203', 'intf': 'et3', 'output': '213'},
 {'device': 'r3', 'input': '300', 'intf': 'et1', 'output': 0},
 {'device': 'r3', 'input': '302', 'intf': 'et2', 'output': '312'},
 {'device': 'r3', 'input': '303', 'intf': 'et3', 'output': '313'}]

 Total traffic per device:
r1 [205, 335]
Total traffic on r1 is 540
r2 [605, 635]
Total traffic on r2 is 1240
r3 [905, 625]
Total traffic on r3 is 1530 
