#!/usr/bin/env python3
# coding=utf-8
#---------------------------------------------------------------
# This script is used to test whether pylib work appropriately.
# It prints basic information and current work directory for
# the user. 
#
# By shashibici (shashibici@gmail.com)
#   11/02/2015
#---------------------------------------------------------------

import sys 
import os
import json
import argparse
from matplotlib import cm
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.patches import Ellipse
from matplotlib.patches import Rectangle
import array
import csv

import matplotlib
#matplotlib.rcParams['pdf.fonttype'] = 42
#matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
#matplotlib.rcParams['text.usetex'] = True

# Useful constants. 
VERSION = sys.version
DIR = os.getcwd()

'''
    data    :   A list of cvs files. For each file,
                first column: 'x', second column: 'value', third column: 'variance'
    config  :   config file that diescribe how to plot.

'''


def plot_set(data, config):
    data_files = data.split(",")
    with open(os.path.join(os.getcwd(), config)) as config_file:
        dics = json.load(config_file)
        grid = dics["plot"]["grid"]
        plots = dics["plot"]["subplots"]
        subplots = {}
        # Draw each of the subplots.
        for plot_id in plots.keys():
            p = plt.subplot(grid["rows"], grid["columns"],
                            (plots[plot_id]["position"][0], plots[plot_id]["position"][1]))
            subplots[plot_id] = p
            data_set = plots[plot_id]["data_set"]
            legends = plots[plot_id]["legends"]
            plot_type = "line"
            if "plot_type" in plots[plot_id]:
                plot_type = plots[plot_id]["plot_type"]
            xvalues = []
            values = []
            errors = []
            lines = {}
            bars = {}
            # Set Default font
            default_font = 'Tahoma'
            if "default_font" in legends:
                default_font = ["default_font"]
            mpl.rc('font', family=default_font)
            # For each input file, look whether this file belongs to this subplot.
            # If it belongs to this subplot, then draw it.
            for file in data_files:
                # If this file does not belong to this subplot, go to the next.
                if file in data_set.keys():
                    y = array.array('f')
                    e = array.array('f')
                    x = array.array('f')
                    # Open the data file
                    with open(os.path.join(os.getcwd(), file)) as csv_file:
                        reader = csv.DictReader(csv_file)
                        for row in reader:
                            x.append(float(row['x'])*float(data_set[file]["xscalar"]))
                            y.append(float(row['value'])*float(data_set[file]["yscalar"]))
                            if "variance" in data_set[file]:
                                if data_set[file]["variance"]:
                                    e.append(float(row['variance'])*float(data_set[file]["yscalar"])/2)
                    xvalues.append(x)
                    values.append(y)
                    errors.append(e)
                    # Draw bars
                    if "bar" == plot_type:
                        print("Draw bars")
                    # Draw horizontal bars
                    elif "barh" == plot_type:
                        # The third parameter is a tuple: (most-left-upper-position, most-right-bottom-position)
                        # The index starts from 1, creasing across rows first
                        bar = subplots[plot_id].barh([70, 20], [100*(1-(787402580.0/1185904361.949152)),100*(1-(820985348.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='\\')
                        #plt.legend([b1, b2, b3], ["200 flows", "400 flows", "600 flows"], loc=(0.36,0.8), prop={"size": 24})
                        #plt.yticks([25,75], ['TCP', 'UDP'])
                        #plt.xlabel("Throughput degradation (%)", fontsize=24)
                        bars[file] = bar
                    # Draw lines
                    else:
                        # Must fields.
                        line, = subplots[plot_id].plot(x, y, data_set[file]["marker"], label=data_set[file]["label"],
                                                       color=data_set[file]["color"], linewidth=data_set[file]["width"],
                                                       markersize=data_set[file]["markersize"])
                        lines[file] = line
                        # Optional fields.
                        if "variance" in data_set[file] and data_set[file]["variance"]:
                            index = 0
                            for yv in y:
                                (_, cap, _) = subplots[plot_id].errorbar(x[index], yv, yerr=e[index], elinewidth=2, capsize=4, color='black')
                                cap[0].set_markeredgewidth(1)
                                cap[1].set_markeredgewidth(1)
                                index += 1
                    # Draw straight line 
                    if "straight" in data_set[file]:
                        straight = data_set[file]["straight"]
                        straight_x1 = straight['x1']
                        straight_y1 = straight['y1']
                        straight_x2 = straight['x2']
                        straight_y2 = straight['y2'] 
                        straight_line_style = None
                        straight_line_color = None
                        straight_line_width = None 
                        if "linestyle"  in straight:
                            straight_line_style = straight['linestyle']
                        if "linewidth"  in straight:
                            straight_line_width = straight['linewidth']
                        if "color"  in straight:
                            straight_line_color = straight['color']
                        
                        straight_line = mlines.Line2D([straight_x1,straight_x2], [straight_y1,straight_y2], linestyle=straight_line_style, linewidth=straight_line_width,color=straight_line_color)
                        fig = plt.gcf()
                        fig.gca().add_line(straight_line)
                    # Draw annotations.
                    if "annotation" in data_set[file]:
                        annotation = data_set[file]["annotation"]
                        if "area" in annotation:
                            area = annotation["area"]
                            centerX = area["x"]
                            centerY = area["y"]
                            width = area["width"]
                            height = area["height"]
                            color = area["color"]
                            linestyle = area["linestyle"]
                            linewidth = area["linewidth"]
                            fill = area["fill"]
                            # draw circle.
                            ellipse = Ellipse((centerX, centerY), width=width, height=height,
                                              linewidth=linewidth, linestyle=linestyle, color=color, fill=fill)
                            fig = plt.gcf()
                            fig.gca().add_artist(ellipse) 
                        if "text" in annotation:
                            text = annotation["text"]
                            string = text["string"]
                            stringX = text["stringX"]
                            stringY = text["stringY"]
                            size = text["size"]
                            color = text["color"]
                            subplots[plot_id].text(stringX, stringY, string, fontsize=size, color=color)
                        if "arrow" in annotation:
                            arrow = annotation["arrow"]
                            startX = arrow["startX"]
                            startY = arrow["startY"]
                            dX = arrow["dX"]
                            dY = arrow["dY"]
                            linewidth = arrow["linewidth"]
                            head_length = arrow["head_length"]
                            head_width = arrow["head_width"]
                            facecolor = arrow["facecolor"]
                            edgecolor = arrow["edgecolor"]
                            subplots[plot_id].arrow(startX,startY,dX,dY,linewidth=linewidth,head_length=head_length,head_width=head_width,facecolor=facecolor,edgecolor=edgecolor)
                        shrink = "1"
#                        subplots[plot_id].arrow(5.1,2,0.5,0,linewidth=4,head_length=0.02*4*1.2,width=0.02,facecolor=color,edgecolor=color)
                        if "arrowprops" in text:
                            arrowprops = text["arrowprops"]
                            color = arrowprops["facecolor"]
                            shrink = arrowprops["shrink"]
                        # draw annotation
#                        subplots[plot_id].annotate(string, xy=(endX, endY), xytext=(stringX, stringY),
#                                     arrowprops=dict(facecolor=color,shrink=shrink), size=size)

            # Must fields.
            if "bar" == plot_type:
                print("TO-DO")
            elif "barh" == plot_type:
                print("TO-DO")
            else:
                subplots[plot_id].set_ylabel(legends["yaxis"]["label"], fontsize=legends["yaxis"]["label_size"])
                subplots[plot_id].set_xlabel((legends["xaxis"]["label"]), fontsize=legends["xaxis"]["label_size"])

            # Optional fields.
            if "lim" in legends["yaxis"]:
                subplots[plot_id].set_ylim(legends["yaxis"]["lim"])
            if "lim" in legends["xaxis"]:
                subplots[plot_id].set_xlim(legends["xaxis"]["lim"])
            if "tick_size" in legends["xaxis"]:
                subplots[plot_id].tick_params(axis='x', labelsize=legends["xaxis"]["tick_size"])
            if "tick_size" in legends["yaxis"]:
                subplots[plot_id].tick_params(axis='y', labelsize=legends["yaxis"]["tick_size"])
            if "tick_struct" in legends["xaxis"]:
                tick_struct = legends["xaxis"]["tick_struct"]
                ticks = tick_struct["ticks"]
                if "bar" == plot_type and "texts" in tick_struct:
                        texts = tick_struct["texts"]
                        plt.xticks(ticks, texts)
                else: 
                    subplots[plot_id].xaxis.set_ticks(ticks)
            if "tick_struct" in legends["yaxis"]:
                tick_struct = legends["yaxis"]["tick_struct"]
                ticks = tick_struct["ticks"]
                if "barh" == plot_type and "texts" in tick_struct:
                        texts = tick_struct["texts"]
                        plt.yticks(ticks, texts)
                else:
                    subplots[plot_id].yaxis.set_ticks(ticks)
            if "title" in legends:
                title = legends["title"]
                text = title["text"]
                fontsize = 32
                loc = -0.22
                if "fontsize" in title:
                    fontsize = title["fontsize"]
                if "loc" in title:
                    loc = title["loc"]
                csfont = {'fontname': default_font}
                if "font" in title:
                    csfont = {'fontname': title["font"]}
                subplots[plot_id].set_title(text, fontsize=fontsize, y=loc, **csfont)
            if "legend" in legends:
                legend = legends["legend"]
                if "loc" in legend:
                    if "bar" == plot_type or "barh" == plot_type:
                        bar_array = []
                        text_array = []
                        for file, bar in bars.items():
                            bar_array.append(bar)
                            text_array.append(data_set[file]["label"])
                        prop = {"size": 24}
                        if "prop" in legend:
                            prop = legend["prop"]
                        plt.legend(bar_array, text_array, loc=legend["loc"], prop=prop)
                    else:
                        handler_map = {}
                        for file, line in lines.items():
                            if "numpoints" in data_set[file]:
                                handler_map[line] = HandlerLine2D(numpoints=data_set[file]["numpoints"])
                            else:
                                handler_map[line] = HandlerLine2D(numpoints=1)
                        prop = {"size": 24}
                        if "prop" in legend:
                            prop = legend["prop"]
                        subplots[plot_id].legend(handler_map=handler_map, loc=legend["loc"], prop=prop)
            if "grid" in legends:
                subplots[plot_id].grid(legends["grid"])


        # The third parameter is a tuple: (most-left-upper-position, most-right-bottom-position)
        # The index starts from 1, creasing across rows first
        #f = plt.subplot(2, 10, (8,20))
        #b1 = f.barh([80, 30], [100*(1-(891783707.0/1185904361.949152)),100*(1-(965411339.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='//')
        #b2 = f.barh([70, 20], [100*(1-(787402580.0/1185904361.949152)),100*(1-(820985348.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='\\')
        #b3 = f.barh([60, 10], [100*(1-(619770486.0/1185904361.949152)),100*(1-(693241941.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='-')
        #csfont = {'fontname': "Times New Roman"}
        #f.set_title("(c) Degradation Percentage", fontsize=30, y=-0.15, **csfont)
        #plt.legend([b1, b2, b3], ["200 flows", "400 flows", "600 flows"], loc=(0.36,0.8), prop={"size": 24})
        #plt.yticks([25,75], ['TCP', 'UDP'])
        #f.set_yticks([25, 75])
        #plt.xlabel("Throughput degradation (%)", fontsize=24)

        #g = plt.subplot(2, 10, (1,7))
        #b1 = g.barh([80, 30], [100*(1-(891783707.0/1185904361.949152)),100*(1-(965411339.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='//')
        #b2 = g.barh([70, 20], [100*(1-(787402580.0/1185904361.949152)),100*(1-(820985348.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='\\')
        #b3 = g.barh([60, 10], [100*(1-(619770486.0/1185904361.949152)),100*(1-(693241941.0/1321699554.350000))], 10, align='center', color=(1/(1+0.0),1/(1+1.0),1/(1+1.0)), hatch='-')
        #g.set_title("(c) Degradation Percentage", fontsize=30, y=-0.15, **csfont)
        #plt.legend([b1, b2, b3], ["200 flows", "400 flows", "600 flows"], loc=(0.36,0.8), prop={"size": 24})
        #plt.yticks([25,75], ['TCP', 'UDP'])


        # After drawing all the subplots, show them.
        plt.show()


def plot_layer_bar(data, config):
    data_files = data.split(",")
    layer_set = {}
    v1 = 1
    bottom = [0,0,0,0]
    bars = []
    names = []
    for file in data_files:
        layer_set[file] = {}
        with open(os.path.join(os.getcwd(), file)) as csv_file:
            value = array.array('f')
            index = array.array('f')
            reader = csv.DictReader(csv_file)
            for row in reader:
                value.append(float(row['value']))
                index.append(float(row['x']))
            layer_set[file]['value'] = value
            layer_set[file]['index'] = index
        layer_set[file]['plot'] = plt.bar(layer_set[file]['index'], layer_set[file]['value'], 0.3, color=str(0.3*v1), bottom=bottom, yerr=2)
        bars.append(layer_set[file]['plot'])
        names.append(file)
        i = 0
        for v in layer_set[file]['value']:
            bottom[i] += v
            i += 1
        v1 += 1
        plt.ylabel('CPU Usage (%)')
        plt.title('Scores by group and gender')
        plt.xticks([1.15, 2.15, 3.15, 4.15],
                   ('HTTP/non-HTTP', 'Protocols/non-Protocols', 'Others/non-Others', 'Monolithic'))
        plt.yticks([20, 40, 60, 80, 100, 120, 140])
        plt.legend(bars, names, loc=0)


    plt.show()

def plot_bar(data, config):
    x2 = array.array('f')
    x3 = array.array('f')
    x4 = array.array('f')
    x5 = array.array('f')
    x6 = array.array('f')
    x7 = array.array('f')
    y2 = array.array('f')
    y3 = array.array('f')
    y4 = array.array('f')
    y5 = array.array('f')
    y6 = array.array('f')
    y7 = array.array('f')
    data_files = ['scale_out.txt', 'merge.txt']

    with open(os.path.join(os.getcwd(), data_files[0])) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            x2.append(float(row['x'])-20)
            x3.append(float(row['x'])-10)
            x4.append(float(row['x']))
            x5.append(float(row['x'])+10)
            x6.append(float(row['x'])+20)
            y2.append(float(row['2']))
            y3.append(float(row['3']))
            y4.append(float(row['4']))
            y5.append(float(row['5']))
            y6.append(float(row['6']))
    with open(os.path.join(os.getcwd(), data_files[1])) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            x7.append(float(row['x']))
            y7.append(float(row['y']))


        # The third parameter is a tuple: (most-left-upper-position, most-right-bottom-position)
        # The index starts from 1, creasing across rows first
        #f1 = plt.subplot(2, 1, (1, 1))

        f2 = plt.subplot(1, 1, (1, 1))

        #b2 = f1.bar(x2, y2, 10, align='center', color=(1/(1+0.0),1/(1+0.0),1/(1+0.0)))
        #b3 = f1.bar(x3, y3, 10, align='center', color=(1/(1+0.1),1/(1+0.1),1/(1+0.1)))
        #b4 = f1.bar(x4, y4, 10, align='center', color=(1/(1+0.4),1/(1+0.4),1/(1+0.4)))
        #b5 = f1.bar(x5, y5, 10, align='center', color=(1/(1+1),1/(1+1),1/(1+1)))
        #b6 = f1.bar(x6, y6, 10, align='center', color=(1/(1+2.6),1/(1+2.6),1/(1+2.6)))
        b7 = f2.bar(x7, y7, 5, align='center', color='blue')

        #f1.legend([b2, b3, b4, b5, b6], ["1", "2", "3", "4", "5"], loc=0, prop={"size": 23})
        #f1.set_xlabel("安全规则组数", fontsize=26)
        #f1.set_ylabel("运行时间 (秒)", fontsize=26)
        #f1.set_xlim([0, 1100])
        #f1.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        #f1.tick_params(axis='x', labelsize=26)
        #f1.set_yticks([0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12])
        #f1.set_ylim([0, 0.12])
        #f1.tick_params(axis='y', labelsize=26)
        #f1.grid(True)

        f2.set_xlabel("负载过低的虚拟防火墙实例数目", fontsize=26)
        f2.set_ylabel("运行时间 (秒)", fontsize=26)
        f2.set_xlim([0, 110])
        f2.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        f2.tick_params(axis='x', labelsize=28)
        f2.set_yticks([0, 0.02, 0.04, 0.06, 0.08, 0.1])
        f2.set_ylim([0, 0.1])
        f2.tick_params(axis='y', labelsize=26)
        f2.grid(True)

        csfont = {'fontname': "Times New Roman"}
        #f1.set_title("(a)", fontsize=30, y=-0.35, **csfont)
        f2.set_title("(b)", fontsize=30, y=-0.35, **csfont)
        plt.show()




def plot_rect(data, config):
    data_files = data.split(",")
    rectangle_sets = {}
    count = len(data_files)
    for file in data_files:
        rectangles = {}
        y = 0
        with open(os.path.join(os.getcwd(), file)) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                index = float(row['x'])
                rectangles[index] = {}
                rectangles[index]['x'] = count
                rectangles[index]['y'] = y
                rectangles[index]['w'] = 30
                rectangles[index]['h'] = float(row['value'])
                y += rectangles[count]['h']
            count -= 1
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal')
        for k, r in rectangles.items():
            print("x=%f,y=%f,w=%f,h=%f" % (r['x'], r['y'], r['w'], r['h']))
            rect = Rectangle((r['x'], r['y']), r['w'], r['h'])
            ax1.add_patch(rect)
        ax1.set_ylim([0, 100])
        ax1.set_xlim([0, 40])

    plt.show()


# Entry:
# --------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', action='store', help='A Json file as a configuration.')

    flavor = parser.add_subparsers(help='Specify the flavor of figures.')

    plot_single_parser = flavor.add_parser('bar', help="Plot a figure with single plot.")
    plot_single_parser.add_argument('-d', '--bar', action='store', help="Specify a data file.")

    plot_set_parser = flavor.add_parser('set', help="Plot a figure with single plot, but multiple lines.")
    plot_set_parser.add_argument('-d', '--set', action='store', help="Specify a list of data files.")

    plot_rect_parser = flavor.add_parser('rect', help="Plot multiple rectangles.")
    plot_rect_parser.add_argument('-d', '--rect', action='store', help="Specify a list of data files.")

    args = vars(parser.parse_args())

    if len(args) < 2:
        print("Type: \"" + sys.argv[0] + " -h\" to watch help information.")
        exit(1)

    config = args['config']
    if "bar" in args:
        data = args['bar']
        plot_bar(data, config)
    elif "set" in args:
        data = args['set']
        plot_set(data, config)
    elif "rect" in args:
        data = args['rect']
        #plot_rect(data, config)
        plot_layer_bar(data, config)
    else:
        print("Unimplemented flavor!")
