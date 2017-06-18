/**
 * Created by neo on 2017/2/21.
 */
// 基于准备好的dom，初始化echarts实例
var Chart = echarts.init(document.getElementById('posert'));

// 指定图表的配置项和数据
var builderJson = {
    "all":{
        "药品收入":{{DrugIncome}},
        "服务收入":
    },
    "Drugs":{
        "药品1":1594,
        "药品4":721,
        "药品3":1608,
        "药品2":925,
        "药品5":2179
    },
    "service":{
        "服务1":2179,
        "服务2":925,
        "服务3":1608,
        "服务4":721,
        "服务5":1982
    },
    "charts":{
        "材料收入":3237,
        "检查收入":2164,
        "验收收入":7561,
        "检验收入":7778,
        "治疗收入":7355,
        "手术收入":2405,
        "挂号收入":1842,
        "其他收入":2090
    },
    "components":{
        "西药收入":2788,
        "中成药收入":9575,
        "中草药收入":9400,
        "基本药物收入":9466,
        "抗生素收入":9266
    },
    "ie":9743
};
var option = {
    tooltip:{},
    legend: {
        data: ['bar1','bar2'],
        align: 'left',
        left: 10
    },
    title:[
        {
            text:'门诊收入构成百分比',
            subtext:'总计 ' + Object.keys(builderJson.all).reduce(function (all, key) {
                return all + builderJson.all[key];
            }, 0) +'.00 元',
            x:'25%',
            y:'5%',
            textAlign:'center'
        },
        {
            text:'服务收入明细',
            subtext:'总计 ' + Object.keys(builderJson.charts).reduce(function (all, key) {
                return all + builderJson.charts[key];
            }, 0),
            x:'85%',
            textAlign:'center'
        },
        {
            text:'药品收入明细',
            subtext:'总计 ' + Object.keys(builderJson.components).reduce(function (all, key) {
                return all + builderJson.components[key];
            }, 0),
            x:'85%',
            y:'47%',
            textAlign:'center'
        },
        {
            text:'服务收入',
            subtext:'总计 ' + Object.keys(builderJson.service).reduce(function (all, key) {
                return all + builderJson.service[key];
            }, 0) + ' 笔',
            x:'60%',
            y:'5%',
            textAlign:'center'
        },
        {
            text:'药品',
            subtext:'总计 ' + Object.keys(builderJson.Drugs).reduce(function (all, key) {
                return all + builderJson.Drugs[key];
            }, 0)+ ' 笔',
            x:'60%',
            y:'55%',

            textAlign:'center'
        }
    ],
    grid:[
        {
            top:50,
            width:'28%',
            bottom:'55%',
            left:"70%",
            containLabel:true
        },
        {
            top:'55%',
            width:'28%',
            bottom:0,
            left:"70%",
            containLabel:true
        }
    ],
    xAxis:[
        {
            type:'value',
            max:Object.keys(builderJson.all).reduce(function (all, key) {
                return all + builderJson.all[key];
            }, 0),
            splitLine:{
                show:false
            }
        },
        {
            type:'value',
            max:Object.keys(builderJson.all).reduce(function (all, key) {
                return all + builderJson.all[key];
            }, 0),
            gridIndex:1,
            splitLine:{
                show:false
            }
        }
    ],
    yAxis:[
        {
            type:'category',
            data:Object.keys(builderJson.charts),
            axisLabel:{
                interval:0,
                rotate:30
            },
            splitLine:{
                show:false
            }
        },
        {
            gridIndex:1,
            type:'category',
            data:Object.keys(builderJson.components),
            axisLabel:{
                interval:0,
                rotate:30
            },
            splitLine:{
                show:false
            }
        }
    ],
    series:[
        {
            type:'pie',
            center:["25%", '50%'],
            data:Object.keys( builderJson.all).map(function (key) {
                return {
                    name:key,
                    value: builderJson.all[key]
                }
            })
        },
        {

            type:'pie',
            radius:[0, '20%'],
            center:['60%', '75%'],
            data:Object.keys(builderJson.Drugs).map(function (key) {
                return {
                    name:key,
                    value:builderJson.Drugs[key]
                }
            })
        },
        {
            type:'pie',
            radius:[0, '20%'],
            center:['60%', '25%'],
            data:Object.keys(builderJson.service).map(function (key) {
                return {
                    name:[key],
                    value:builderJson.service[key]
                }
            })
        },
        {
            name: 'bar1',
            type:'bar',
            stack:'chart',
            z:3,
            label:{
                normal:{
                    position:'right',
                    show:true
                }
            },
            data:Object.keys(builderJson.charts).map(function (key) {
                return builderJson.charts[key];
            })
        },
        {
            name: 'bar2',
            type:'bar',
            stack:'component',
            xAxisIndex:1,
            yAxisIndex:1,
            z:3,
            label:{
                normal:{
                    position:'right',
                    show:true
                }
            },
            data:Object.keys(builderJson.components).map(function (key) {
                return builderJson.components[key];
            })
        }

    ]
}
// 使用刚指定的配置项和数据显示图表。
Chart.setOption(option);