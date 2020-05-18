

//First run this file to find fft of sinc function it stores results in Q3supl.txt
//After that run Q3pysupl.py tomlook  at the graph
#include<stdio.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#include<stdlib.h>
#include<math.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])


float sinc(float x)
{
 if(x==0)
  return 1;
 else
  return(sin(x)/x);
}


void main ()
{

  const int n = 128;
  float xmin = -50.0,xmax=50.0,dx;

  dx = (xmax-xmin)/(n-1);
  float cf =(dx/sqrt(2*M_PI));   //Multiplication factor
  double dft[2*n];

  float rf[n];
  float imf[n];
  float k[n];

  FILE *myFile;



  for (int i = 0; i < n; i++)
    {
      REAL(dft,i) = sinc( xmin + i*dx);
      IMAG(dft,i) = 0.0;
    }


  gsl_fft_complex_wavetable * wavetable;
  gsl_fft_complex_workspace * workspace;


  wavetable = gsl_fft_complex_wavetable_alloc (n);
  workspace = gsl_fft_complex_workspace_alloc (n);


  gsl_fft_complex_forward (dft, 1, n, wavetable, workspace);



   for (int i = 0; i < n; ++i)
 {
   if(i<(n/2))
    k[i]=(i/(n*dx))*(2*M_PI);

   else k[i]=((i-n)/(n*dx))*(2*M_PI);

    rf[i]=cos(-k[i]*xmin);
    imf[i]=sin(-k[i]*xmin);
 }



  for (int i = 0; i < n; ++i)
 {
   REAL(dft,i)=cf*(rf[i]*REAL(dft,i)-imf[i]*IMAG(dft,i));
   IMAG(dft,i)=cf*(rf[i]*IMAG(dft,i)+imf[i]*REAL(dft,i));
 }

    for (int i = 0; i < n; ++i)
    {
       printf ("\n %f + j(%f) \n", REAL(dft,i),IMAG(dft,i));
    }



  myFile = fopen("Q3rl.txt", "w");

    for (int i = 0; i < n; i++)
    {
        fprintf(myFile,"%f  %f \n",k[i],REAL(dft,i));
    }

  fclose(myFile);

  gsl_fft_complex_wavetable_free (wavetable);
  gsl_fft_complex_workspace_free (workspace);



}
