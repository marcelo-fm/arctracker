{ 
"displayFieldName" : "<displayFieldName>",
"fieldAliases" : {
  "<fieldName1>" : "<fieldAlias1>",
  "<fieldName2>" : "<fieldAlias2>"
},
"geometryType" : "<geometryType>",
"hasZ" : <true|false>,  //Added at 10.1
"hasM" : <true|false>,   //Added at 10.1
"spatialReference" : <spatialReference>,
"fields": [
            {
                "name": "<field1>",
                "type": "<field1Type>",
                "alias": "<field1Alias>"
            },
            {
                "name": "<field2>",
                "type": "<field2Type>",
                "alias": "<field2Alias>"
            }
        ],
 "features": [
            {
                "geometry": {
                    <geometry1>
                },
                "attributes": {
                    "<field1>": <value11>,
                    "<field2>": <value12> 
                } 
            },
            {
                "geometry": {
                    <geometry2>
                },
                "attributes": {
                    "<field1>": <value21>,
                    "<field2>": <value22> 
                } 
            }
        ]
}