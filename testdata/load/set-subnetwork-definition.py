'''****************************************************************************
Name:        SetSubnetworkDefinition.py
Description: This script sets the subnetwork definition for a tier in a Utility Network
Created by:  Esri
****************************************************************************'''

# Import required modules        
import arcpy

# Set local variables
in_utility_network = "ElectricDistribution"
domain_network = "ElecDist"
tier_name = "Medium Voltage"
support_disjoint_subnetwork = "SUPPORT_DISJOINT"
valid_devices = "'CircuitBreaker/Unknown';'CircuitBreaker/Air powered';'NetworkProtector/Unknown';'NetworkProtector/NetworkProtector';'Transformer/Unknown';'Transformer/Buck boost';'Transformer/Single-phase overhead';'Transformer/Single-phase padmounted';'Transformer/Three-phase padmounted';'Transformer/Power';'Transformer/Step';'Transformer/Vault'"
valid_subnetwork_controller = "'CircuitBreaker/Unknown';'CircuitBreaker/Air powered'"
valid_lines = "'Busbar/Unknown';'Busbar/Busbar';'Connector/Unknown';'Connector/Connector';'LowVoltage/Unknown';'LowVoltage/Overhead';'LowVoltage/Underground';'MediumVoltage/Unknown';'MediumVoltage/Single-phase overhead';'MediumVoltage/Two-phase overhead';'MediumVoltage/Three-phase overhead';'MediumVoltage/Single-phase underground';'MediumVoltage/Two-phase underground';'MediumVoltage/Three-phase underground';'IsolatedNeutral/Unknown';'IsolatedNeutral/Concentric neutral';'IsolatedNeutral/Neutral';'SubTransmission/Unknown';'SubTransmission/Overhead';'SubTransmission/Underground'"
aggregated_line = "'Busbar/Unknown';'Busbar/Busbar';'MediumVoltage/Unknown';'MediumVoltage/Single-phase overhead';'MediumVoltage/Two-phase overhead';'MediumVoltage/Three-phase overhead';'MediumVoltage/Single-phase underground';'MediumVoltage/Two-phase underground';'MediumVoltage/Three-phase underground'"
diagram_template = "Basic"
summaries = ""
condition_barriers = "'Device Status' IS_EQUAL_TO SPECIFIC_VALUE 'Opened' #"
function_barriers = ""
include_barriers = "INCLUDE_BARRIERS"
traversability_scope = "BOTH_JUNCTIONS_AND_EDGES"
propagators = ""

# Run the SetSubnetworkDefinition tool
arcpy.un.SetSubnetworkDefinition(in_utility_network, 
                                 domain_network, 
                                 tier_name, 
                                 support_disjoint_subnetwork, 
                                 valid_devices, 
                                 valid_subnetwork_controller, 
                                 valid_lines, 
                                 aggregated_line, 
                                 diagram_template, 
                                 summaries, 
                                 condition_barriers, 
                                 function_barriers, 
                                 include_barriers, 
                                 traversability_scope, 
                                 propagators)