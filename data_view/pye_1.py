from pyecharts import *
from data_view import learn_2
from example.commons import Faker
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType

le2 =learn_2

def mk_bar():

    # //设置行名
    columns = ['上海','北京','杭州']
    # //设置数据
    data2 = []
    for i in columns:
        data2.append(round(le2.get_avr(i),3))
        print(data2)
    # //设置柱状图的主标题与副标题
    bar = Bar("柱状图", "PHP开发工程师各地平均薪资")
    # //添加柱状图的数据及配置项
    bar.add("月薪/万", columns, data2, mark_line=["average"], mark_point=["max", "min"])

    # 折线图
    line = Line("折线图", "一年的降水量与蒸发量")
    # // is_label_show是设置上方数据是否显示
    line.add("月薪/万", columns, data2, is_label_show=True)
    # //生成本地文件（默认为.html文件）
    grid = Grid()
    # // 设置两个图表的相对位置
    grid.add(bar, grid_left="50%")
    grid.add(line, grid_right="50%")
    grid.render('grid.html')

def mk_pie():
    # // 设置主标题与副标题，标题设置居中，设置宽度为900
    pie = Pie("饼状图", "PHP开发工程师职位数量分布图", title_pos='center', width=900)
    columns = ['上海','北京','杭州']
    # // 加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
    # pie.add("降水量", columns, data1, center=[25, 50], is_legend_show=False)
    data1 = []
    for i in columns:
        data1.append(le2.get_num(i))
        print(data1)
    # // 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
    pie.add("职位数", columns, data1, center=[75, 50], is_legend_show=False, is_label_show=True)
    # // 保存图表
    pie.render('pie.html')


def mk_line():
    # //设置行名
    columns = ['上海','北京','杭州']
    # //设置数据
    data2 = []
    for i in columns:
        data2.append(round(le2.get_avr(i),3))
        print(data2)
    # 折线图
    line = Line("折线图", "PHP开发工程师各地平均薪资")
    # // is_label_show是设置上方数据是否显示
    line.add("月薪/万", columns, data2, is_label_show=True)
    line.render('line.html')
    return line

def mk_scatter():
    scatter = Scatter("散点图", "PHP开发工程师各地平均薪资")
    # // xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
    data2 = []
    data1 = ['上海','北京','杭州']
    for i in data1:
        data2.append(round(le2.get_avr(i),3))
        print(data2)
    scatter.add("PHP开发工程师各地平均薪资分布", data1, data2, xaxis_name="地区", yaxis_name="月薪/万",
                yaxis_name_gap=40)
    scatter.render('scatter.html')

def map_visualmap() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c

