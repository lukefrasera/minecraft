#ifndef VIEW_H
#define VIEW_H

#include <QGLWidget>
#include <QTimer>
#include <QTime>

class view : public QGLWidget
{
    Q_OBJECT
public:
    explicit view(QWidget *parent = 0);
    ~view();
    
private:
    QTime time;
    QTimer timer;
    float rotX, rotY;


    void initializeGL();
    void paintGL();
    void resizeGL(int w, int h);

    void mousePressEvent(QMouseEvent *);
    void mouseMoveEvent(QMouseEvent *);
    void mouseReleaseEvent(QMouseEvent *);

    void keyPressEvent(QKeyEvent *);
    void keyReleaseEvent(QKeyEvent *);
    void perspective( float fovyInDegrees, float aspectRatio, float znear, float zfar);

signals:
    
public slots:
    void tick();
    
};

#endif // VIEW_H
