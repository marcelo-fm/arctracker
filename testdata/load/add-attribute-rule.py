'''****************************************************************************
Name:        AddAttributeRule_example3.py
Description: This script adds a validation rule to a feature class
Created by:  Esri
****************************************************************************'''

# Import required modules        
import arcpy

# Set local variables
in_table = "C:\\MyProject\\sdeConn.sde\\progdb.user1.GasPipes"
name = "validationRuleMaxOP"
rule_type = "VALIDATION"
script_expression = "$feature.OPERATINGPRESSURE < 300"
error_number = 3001
error_message = "Maximum operating pressure exceeded"
description = "Validation rule: max operating pressure value"
subtype = "Coated Steel"
batch = "BATCH"
severity = 3
tags = "OP;MAXOP"

# Run the AddAttributeRule tool
arcpy.management.AddAttributeRule(in_table, name, rule_type, 
                                  script_expression, "", "", 
                                  error_number, error_message, 
                                  description, subtype, "", "", 
                                  batch, severity, tags)