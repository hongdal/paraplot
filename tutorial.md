##Example of a configuration file
```
{
    # Definition of subplots. (MUST)
    "plot": {
        # Grid. 
        "grid": {
            "rows": 2,
            "columns": 9
        },
        # Associate plots with positions.
        "subplots": {
            "subplot_id_1": {
                # The first element in the array indicates position of the left-upper corner
                # The second element in the array indicates the position of the right-bottom conner
                "position": [1,6],
                # Description of figure. (MUST)
                "legends": {
                    # title. (OPT)
                    "title": {
                        # (MUST)
                        "text": "Install/Delete security policies",
                        # (OPT) set to 32 by default
                        "fontsize": 32,
                        # (OPT)
                        "font": "Times New Roman",
                        # if < 0, then the title will show on the bottom; otherwise on the top.
                        # (OPT) On top of the figure by default.
                        "loc": -0.2
                    },
                    # (OPT) - Tahoma by default
                    "default_font": "Tahoma",
                    # grid.
                    "grid": true,
                    # legend properties. (OPTIONAL)
                    "legend": {
                        #location
                        "loc": 0,
                        #property (type of string)
                        "prop": {
                            "size": 28
                        }
                    },
                    # X axis. (MUST)
                    "xaxis": {
                        # xlabel. (MUST)
                        "label": "Time (million second)",
                        # limitation of X.
                        "lim": [100, 500],
                        # tick size.
                        "tick_size": 24,
                        # label font size. (MUST)
                        "label_size": 28,
                        # ticks_struct (OPTIONAL)
                        "tick_struct" : 
                        {
                            # (MUST)
                            "ticks" : [1,2,3,4,5],
                            # (OPTIONAL)
                            "texts" : ["string1", "string2"]
                        }
                        
                    },
                    # Y axis. (MUST)
                    "yaxis": {
                        # ylabel
                        "label": "Number of instances",
                        # limitation of Y
                        "lim": [0, 1000],
                        # tick size
                        "tick_size": 24,
                        # label font size
                        "label_size": 28
                    }
                },
                "data_set": {
                    # Description of a set of data. (MUST)
                    "data1.txt": { 
                        # Draw a straight line.  (OPT)
                        "straight" : {
                            # start point. 
                            "x1" : 50,
                            "y1" : 2, 
                            # end point. 
                            "x2" : 50, 
                            "y2" : 8,
                            # line type. 
                            "linestyle" : "--",
                            "linewidth" : 10,
                            "color" : "black"
                        },
                        # Name shown in legend. (MUST)
                        "label": "fw1_from_client_11",
                        # Marker of the line. (MUST)
                        "marker": "--",
                        # color. (MUST)
                        "color": "red",
                        # width. (MUST)
                        "width": 3,
                        # marker size. (MUST)
                        "markersize": 6,
                        # 'x' will multiple this scalar. (MUST)
                        "xscalar": 1.0,
                        # 'y' will multiple this scalar. (MUST)
                        "yscalar": 0.000000001,
                        # How many points for legend display. (OPT)
                        "numpoints": 1
                        # annotation of this dataset. (OPT)
                        "annotation": {
                            # draw an area of interest. (OPT)
                            "area": {
                                # center x
                                "x": 100,
                                # center y
                                "y": 200,
                                # width
                                "width": 2,
                                # height
                                "height": 1,
                                # valid values : ['solid', 'dashed', 'dashdot', 'dotted']
                                "linestyle": "solid",
                                "linewidth": 3,
                                "color": "green",
                                # fill the area or not
                                "fill": false
                            },
                            # Annotation (MUST)
                            "text": {
                                # The string that will be printed.
                                "string": "something...",
                                # The position of the string that will be printed.
                                "stringX": 300,
                                "stringY": 400,
                                # the point that will be pointed by the arrow.
                                "endX": 100,
                                "endY": 200,
                                # text size
                                "size": 40,
                                # property of the arrow. (OPT)
                                "arrowprops": {
                                    "facecolor": "blue",
                                    "shrink": 0.05
                                }
                            }
                        }
                    },
                    # Description of a set of data. (MUST)
                    "data2.txt": {
                        # Name shown in legend. (MUST)
                        "label": "fw1_from_client_11",
                        # Marker of the line. (MUST)
                        "marker": "--",
                        # color. (MUST)
                        "color": "red",
                        # width. (MUST)
                        "width": 3,
                        # marker size. (MUST)
                        "markersize": 6,
                        # 'x' will multiple this scalar.
                        "xscalar": 1.0,
                        # 'y' will multiple this scalar.
                        "yscalar": 0.000000001,
                        # How many points for legend display. (OPT)
                        "numpoints": 1
                    }
                }
            },
             "subplot_id_2": {
                # The first element in the array indicates position of the left-upper corner
                # The second element in the array indicates the position of the right-bottom conner
                "position": [1,6],
                # Description of figure. (MUST)
                "legends": {
                    # title. (MUST)
                    "title": {
                        # (MUST)
                        "text": "Install/Delete security policies",
                        # (OPT) set to 32 by default
                        "fontsize": 32,
                        # if < 0, then the title will show on the bottom; otherwise on the top.
                        # (OPT) On top of the figure by default.
                        "loc": -0.2
                    },
                    # grid.
                    "grid": true,
                    # legend properties. (OPTIONAL)
                    "legend": {
                        #location
                        "loc": 0,
                        #property (type of string)
                        "prop": {
                            "size": 28
                        }
                    },
                    # X axis. (MUST)
                    "xaxis": {
                        # xlabel. (MUST)
                        "label": "Time (million second)",
                        # limitation of X.
                        "lim": [100, 500],
                        # tick size.
                        "tick_size": 24,
                        # label font size. (MUST)
                        "label_size": 28,
                        # ticks.
                        "ticks": [1,2,3,4,5]
                    },
                    # Y axis. (MUST)
                    "yaxis": {
                        # ylabel
                        "label": "Number of instances",
                        # limitation of Y
                        "lim": [0, 1000],
                        # tick size
                        "tick_size": 24,
                        # label font size
                        "label_size": 28
                    }
                },
                "data_set": {
                    # Description of a set of data. (MUST)
                    "data1.txt": {
                        # Name shown in legend. (MUST)
                        "label": "fw1_from_client_11",
                        # Marker of the line. (MUST)
                        "marker": "--",
                        # color. (MUST)
                        "color": "red",
                        # width. (MUST)
                        "width": 3,
                        # marker size. (MUST)
                        "markersize": 6,
                        # 'x' will multiple this scalar. (MUST)
                        "xscalar": 1.0,
                        # 'y' will multiple this scalar. (MUST)
                        "yscalar": 0.000000001,
                        # How many points for legend display. (OPT)
                        "numpoints": 1
                        # annotation of this dataset. (OPT)
                        "annotation": {
                            # draw an area of interest. (OPT)
                            "area": {
                                # center x
                                "x": 100,
                                # center y
                                "y": 200,
                                # width
                                "width": 2,
                                # height
                                "height": 1,
                                # valid values : ['solid', 'dashed', 'dashdot', 'dotted']
                                "linestyle": "solid",
                                "linewidth": 3,
                                "color": "green",
                                # fill the area or not
                                "fill": false
                            },
                            # Annotation (MUST)
                            "text": {
                                # The string that will be printed.
                                "string": "something...",
                                # The position of the string that will be printed.
                                "stringX": 300,
                                "stringY": 400,
                                # the point that will be pointed by the arrow.
                                "endX": 100,
                                "endY": 200,
                                # text size
                                "size": 40,
                                # property of the arrow. (OPT)
                                "arrowprops": {
                                    "facecolor": "blue",
                                    "shrink": 0.05
                                }
                            }
                        }
                    },
                    # Description of a set of data. (MUST)
                    "data2.txt": {
                        # Name shown in legend. (MUST)
                        "label": "fw1_from_client_11",
                        # Marker of the line. (MUST)
                        "marker": "--",
                        # color. (MUST)
                        "color": "red",
                        # width. (MUST)
                        "width": 3,
                        # marker size. (MUST)
                        "markersize": 6,
                        # 'x' will multiple this scalar.
                        "xscalar": 1.0,
                        # 'y' will multiple this scalar.
                        "yscalar": 0.000000001,
                        # How many points for legend display. (OPT)
                        "numpoints": 1
                    }
                } # end of data_set
            } # end of subplot
        }# end of subplots
    }# end of plot
}
```
## References
* [Draw an ellipse in python](http://matplotlib.org/api/patches_api.html#matplotlib.patches.Ellipse)
* [Draw an annotation in python](http://matplotlib.org/api/pyplot_api.html?highlight=annotate#matplotlib.pyplot.annotate)
