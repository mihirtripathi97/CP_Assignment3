//Important introductions
//Use =   -lfft3f -lm flag for this program

// This program takes in X values from a text file Q2.supl.txt which is created by running python code for Q1 (It has also been uploaded
// in github repository along with the code. It then calculates F(X[i]) which is the sinc function.
// After that it calculates its dft and prints real part of fft into another text file  named Q2rl.txt (also included in github repositary)
// In order to compare the results of this code with the results of Q1 code made in python one needs to run code in Q2pysupl.py
// This will take values of fft stored in Q2rl.c and plot it along with fft calculated in Q1
// Since the file Q2supl.txt has 64 entries the dft calculated here also is for 64 values where X belongs to [-50, 50] if the nuber 64 is changed in Q1
// then the Q2supl.txt will also have different number of entries. So if X array length is changed in Q1 for checking purpose,
// then that need to reflect here and variable int n 's value will need to be changed correspondingly
// Although code is designed to calculate dft irrespective of n being odd or even , it is advised to keep n even.


#include<stdio.h>
#include<math.h>
#include<complex.h>
#include<fftw3.h>


float Sinc(float X)
{
    float y;
    if(X==0)
    {
        y = 1.0;
    }
    else
        y = sin(X)/X;
    return(y);
}
void main()
{
    int n = 64;
    float X[n],a,b,c,d,rF,cF;

    float karr[n];
    fftwf_complex out[n],in[n];
    fftwf_plan p;


    FILE *myFile;
    myFile = fopen("Q2supl.txt", "r");

    for (int i = 0; i < n; i++)
    {
        fscanf(myFile, "%f", &X[i]);
    }

    float dx = fabs(X[1]-X[0]);
/*
    for(int i = 0; i<n;++i)
    {

        printf(" i= %d X = %f\n",i, X[i]);        // Prints X[i]

    }
*/

    for(int i = 0; i<n; ++i)
    {
        in[i] = Sinc(X[i]);    //Important
    }


    p = fftwf_plan_dft_1d(n, in, out,FFTW_FORWARD,FFTW_ESTIMATE);
    fftwf_execute(p);

    for(int i = 0; i<n; ++i)
    {
        printf("dft = %f +i%f \n",creal(out[i]),cimag(out[i]));
    }



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
/*
    for(int i=0;i<n;++i)
    {
        printf("\n karr = %f\n",karr[i]);
    }
*/
    for(int i=0;i<n;++i)
    {
        a = cos(-karr[i]*X[0]);
        b = sin(-karr[i]*X[0]);
        c = creal(out[i]);
        d = cimag(out[i]);

        rF = (a*c - b*d);
        cF = (a*d + b*c);

        

        out[i] = dx*( rF )/sqrt(2.0*M_PI) + I*dx*( cF )/sqrt(2.0*M_PI);
    }

    for(int i = 0; i<n;++i)
    {

        printf("%f + %fj\n", crealf(out[i]), cimagf(out[i]));
    }

    myFile = fopen("Q2rl.txt", "w");

    for (int i = 0; i < n; i++)
    {
        fprintf(myFile, "%f %f\n", karr[i],creal(out[i]));
    }


}
