#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv/cv.h>
#include <opencv2/imgproc/imgproc.hpp>

#include <qgraphicsscene.h>
#include <QPixmap>
#include <QImage>
#include <QApplication>
#include <QFileDialog>
#include <QMainWindow>
#include <QTimer>
#include <QtGui>
#include <QDir>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QPixmap>
#include <QDebug>
#include <QTextStream>
#include <vector>
#include <iostream>


using namespace  std;
using namespace  cv;


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
private:
    int temporal=0;
    int valorCambioImagen=0;



    Mat img;
    Mat Histograma;
    Mat gray;

    QImage imdisplay;
    QImage HistogramaDisplay;

    QTimer *Timer;

    int Flag=0;
    Size tam_imagen;
    Ui::MainWindow *ui;


    QImage qimageOriginal;
    QImage QimageProces;

    QPixmap Loadimage;
    QImage *imageObject;
    QGraphicsScene *scene;

    string PathImage;
    QString filename;

    //QImage image(128, 128);

public:
    explicit MainWindow(QWidget *parent = nullptr);
    //funciones
    void operacionAritmetica(int val,  char ope);
    void histograma();


public slots:
    void Display_Image();
private slots:
    //slider
    void on_horizontalSlider_valueChanged(int value);

    //open image clicked
    void on_OpenImage_clicked();

    //funciones de imagenes
    void on_Griss_clicked();
    void on_Gamma_clicked();
    void on_Equalisacion_clicked();
    void on_Save_clicked();
    void on_Contraste_valueChanged(int value);
    void on_Divicion_valueChanged(int value);
};

#endif // MAINWINDOW_H
