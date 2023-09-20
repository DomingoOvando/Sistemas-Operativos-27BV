#!/bin/bash


show_menu() {
    clear
    echo "Menú de opciones:"
    echo "1. Imprime mi arbol de mango"
    echo "2. Imprime mi mundo de caramelo"
    echo "3. imprime mi name we"
    echo "4. BYE EZZ"
    echo "5. GG NO JUNGLA NI ADC"
}

while true; do
    show_menu

    read -p "Aver elige " choice

    case $choice in
        1)
            ./arbol.sh
            read -p "Presione Enter para continuar..."
            ;;
        2)
            ./mundo.sh
            read -p "Presione Enter para continuar..."
            ;;
        3)
            ./name.sh
            read -p "Presione Enter para continuar..."
            ;;
        4)
            echo "SAlte de mi programa"
            exit 0
            ;;
        *)
            echo "Adivina la opcion chamaco "
            read -p "Presione Enter para continuar..."
            ;;
    esac
done
