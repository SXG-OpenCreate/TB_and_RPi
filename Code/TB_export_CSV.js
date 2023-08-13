/*---------------------------------------------------------
*
* 範例:Thingsboard>dashboard>widgets>Timeseries Line Chart
*
----------------------------------------------------------*/

//UTC時間 格式化為 本地時間
function formatDateTime(utcDateObj){
  
    const offset = (8*3600*1000);//UTC +8時
    const localTimeInMillis = new Date(utcDateObj.getTime() + offset);
    const localTime = new Date(localTimeInMillis);
    
    //用字串截取的方式 從localTime裡面 "時"的字串
    var dateTimeStr = localTime.toISOString();
    var timePart = dateTimeStr.split('T')[1];
    var hours = timePart.split(':')[0];

    //獲取 年月日
    var year = localTime.getUTCFullYear();
    var month = ('0'+(localTime.getMonth() + 1)).slice(-2);
    var day =   ('0'+localTime.getDate()).slice(-2);

    //獲取 分秒
    var minutes = ('0'+localTime.getMinutes()).slice(-2);
    var seconds = ('0'+localTime.getSeconds()).slice(-2);
  
    return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
}


//widgets接收的裝置數據 在widgetContext物件裡面
var widgetData =   widgetContext;

//生成csv文件，編碼為utf-8
var csvContent = "data:text/csv;charset=utf-8,";

//建立csv文件 第一行標題
csvContent += "timestamp,"
var i=0;
var j=0;
for(i=0;i<widgetData.data.length;i++)
{
    csvContent += widgetData.data[i].dataKey.name;
    csvContent +=","
}
csvContent += "\n";



//獲取格式化後的時間
var timestamp = formatDateTime(new Date(widgetData.data[0].data[0][0]));

//處理 全部 keys:value
widgetData.data[0].data.forEach((outerElement,j) => {
    csvContent += formatDateTime(new Date(outerElement[0])) + ",";    
    widgetData.data.forEach((innerElement) => {
        csvContent += innerElement.data[j][1] + ",";    
    });
    csvContent += "\n";
});
        
var encodedUri = encodeURI(csvContent);
window.open(encodedUri);
