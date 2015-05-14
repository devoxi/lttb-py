#!/usr/bin/env bash

if [ -z $1 ] || ! [ -f $1 ]; then
    echo "Missing or incorrect input file"
    exit
fi

if [ -z $2 ]; then
    echo "Missing output file"
    exit
fi

if [ -z $3 ]; then
    echo "Missing title"
    exit
fi

gnuplot << EOF
    # reset config
    reset
    
    # define data delimiter
    set datafile separator ","
    
    # define terminal
    set terminal pngcairo size 720,480 enhanced font 'Verdana,10'
    
    # define axis
    # remove border on top and right and set color to gray
    set style line 11 lc rgb '#808080' lt 1
    set border 3 back ls 11
    set tics nomirror
    
    # define grid
    set style line 12 lc rgb '#808080' lt 0 lw 1
    set grid back ls 12
    
    # define legend
    set key off
    
    # define line styles
    set style line 1 lt 1 lc rgb '#483D8B' lw 2 # Color: DarkSlateBlue
    set style line 2 lt 1 lc rgb '#3CB371' lw 2 # Color: MediumSeaGreen
    set style line 3 lt 1 lc rgb '#CD853F' lw 2 # Color: Peru
    set style line 4 lt 1 lc rgb '#663399' lw 2 # Color: RebeccaPurple
    set style line 5 lt 1 lc rgb '#6B8E23' lw 2 # Color: OliveDrab
    set style line 6 lt 1 lc rgb '#DC143C' lw 2 # Color: Crimson
    set style line 7 lt 1 lc rgb '#FF4500' lw 2 # Color: OrangeRed
    
    # define ranges
    set yrange [0:500]
    
    # define output
    set output "$2"
    # define labels
    set title "${@:3}"
    set xlabel "Time (s)"
    set ylabel "Y axis"
    # plotting
    plot "$1" using 1:2 ls 6 with lines
EOF