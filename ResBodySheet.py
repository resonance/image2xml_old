#ResBodySheet contains a sequence of dictionaries (ReferenceBody Measurements, Trim Measurements, Angle Measurements)
#Dictionaries provide built in functions for manipulaiton to add or delete entires


metaData = {
    'XML_Verion': 1.0,
    'Units': 'inch',
    'Gender': 'Female',
}

Reference_Body = {
    'height': 67,
    'height_neck_back': 57.5
    'height_scapula': 50.5
    'height_armpit': 49
    'height_waist_side': 41
    'height_hip': 33.5
    'height_gluteal_fold': 31
    'height_knee': 19
    'height_calf': 12.75
}

Resonance_Tokens = {
    'Label_coordinates' : 'mx=\".1\" my=\".1\"',
    'alongLine': 'type=\"alongLine\" typeLine=\"none\"',
    'interactive': 'type=\"simpleInteractive\"',
    'pointOFContact': 'type=\"pointOfContact\"',
    'endLine': 'type=\"endLine\" typeLine=\"hair\"'
}

Trim_Measurements = {
    'Elastic_Width': 3
}

Angle_Measurements = {
    'right': [0, 360],
    'down': 270,
    'up': 90,
    'left': 180
}
