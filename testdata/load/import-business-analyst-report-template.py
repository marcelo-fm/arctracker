import arcpy
arcpy.ba.ImportBusinessAnalystReportTemplate(
    online_report_template_id="33bcaa1e97fc4b9ba7fc68e14402a10f",
    output_folder=r"C:\ArcGIS\Business Analyst Templates",
    dataset_id="USA_ESRI_2022",
    config='{"downloadConfig":[{"id":"023871b31068415cbc0340fdd3ec5ba7","download":true,"path":"","name":"San Francisco Spending"}]}')