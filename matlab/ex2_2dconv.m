clc;
clear all;
close all;

z = imread('apple.png');
zbw = rgb2gray(z);
imshow(zbw);