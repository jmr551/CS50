#include <iostream.h>
using namespace std;


// Que el usuario ingrese un numero entre 100 y 200. Si el numero es valido, imprimir el doble.
// Imprimir un error en caso contrario.
int main()
{
    float n;
    cin << n;

    if (n>=100 and n<=200) //Si n está entre 100 y 200
    {
        cout<<2*n;
    }
    else //Si no está entre 100 y 200
    {
        cout<<"El numero no esta entre 100 y 200.";
    }
}