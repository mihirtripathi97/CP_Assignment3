//Important introductions
//Use =   -lfft3 -lm flag for this program

// This program takes in X values from a text file Q4.supl.txt (It has been uploaded
// in github repository along with the code). It then calculates F(X[i]) which is the gauss function (X varies from -10 to 10).
// After that it calculates its dft and prints real part of fft into another text file  named Q4rl.txt (also included in github repositary)
// In order to compare the results of this code with the results of Q1 code made in python one needs to run code in Q2pysupl.py
// This will take values of fft stored in Q2rl.c and plot it along with fft calculated in Q1
// Since the file Q4supl.txt has 64 entries the dft calculated here also is for 64 values where X belongs to [-10, 10]
// Although code is designed to calculate dft irrespective of n being odd or even , it is advised to keep n even.





#include<stdio.h>
#include<math.h>
#include<complex.h>
#include<fftw3.h>


double Gauss(double x)
{
    double y;

    y = exp(-x*x);

    return(y);

}
void main()
{
    int n = 64;
    double X[n],a,b,c,d,rF,cF;
    double karr[n];

    fftw_complex out[n],in[n];
    fftw_plan p;


    FILE *myFile;
    myFile = fopen("Q4supl.txt", "r");

    for (int i = 0; i < n; i++)
    {
        fscanf(myFile, "%lf", &X[i]);
    }

    double dx = fabs(X[1]-X[0]);

    for(int i = 0; i<n;++i)
    {

        //printf(" i= %d X = %f\n",i, X[i]);

    }


    for(int i = 0; i<n; ++i)
    {
        out[i] = 0 + 0*I;
    }



    for(int i = 0; i<n; ++i)
    {
        in[i] = Gauss(X[i]) + 0*I;    //Important
    }



    for(int i = 0; i<n;++i)
    {
        printf("%lf + i%lf\n",creal(in[i]),cimag(in[i]));
    }



    p = fftw_plan_dft_1d(n, in, out,FFTW_FORWARD,FFTW_ESTIMATE);
    fftw_execute(p);
/*
    for(int i = 0; i<n; ++i)
    {
        printf("%f\n",creal(out[i]));
    }
*/



    int j;
    j = ceil((n-1)/2);

    for(int i=0;i<((n/2)+1);++i)
    {
        if(n%2 == 0)
        {
            karr[i] = 2.0*M_PI*(i)/(n*dx);
            karr[n-1-i] = -2.0*M_PI*(i+1)/(n*dx);
        }
        else
        {
            karr[i] = 2.0*M_PI*(i)/(n*dx);
            karr[j+i] = -2.0*M_PI*(n-1+i)/(2*n*dx);

        }

    }

    for(int i=0;i<n;++i)
    {
        a = cos(-karr[i]*X[0]);
        b = sin(-karr[i]*X[0]);
        c = creal(out[i]);
        d = cimag(out[i]);

        rF = (a*c - b*d);
        cF = (a*d + b*c);

        //printf("\n rf = %f",rF);

        out[i] = dx*( rF )/sqrt(2.0*M_PI) + I*dx*( cF )/sqrt(2.0*M_PI);
    }


    printf("\nFFT is : \n");
    for(int i = 0; i<n;++i)
    {

        printf("%lf + %lfj\n", creal(out[i]), cimag(out[i]));
    }

    myFile = fopen("Q4rl.txt", "w");

    for (int i = 0; i < n; i++)
    {
        fprintf(myFile, "%lf %lf\n", karr[i],creal(out[i]));
    }






}
