Bootstrap: docker
From: ufscar/ubuntu_ompi:latest

%help
Exemplo para o uso do serviço de nuvem da UFSCar usando container Singularity com OpenMPI

%files
    # Copie seus arquivos
    #./Source/* /opt

%post
    # Exceute comandos, por exemplo para compilar seus programas
    # echo "Compilando programas..."
    # cd /opt && gcc sum_seq.c -o sum_seq && mpicc sum_par.c -o sum_par && mpicc poisson.c -o poisson

%runscript
    # Comando a ser executado quando o container for executado
    # /opt/poisson

%test
    # Testes de consistência
    # [ -f /opt/sum_seq ] && echo "\e[31mArquivo sum_seq existe!\e[0m" || echo "\e[31m\aERRO: Arquivo sum_seq não existe!\e[0m"
    # [ -f /opt/sum_par ] && echo "\e[31mArquivo sum_par existe!\e[0m" || echo "\e[31m\aERRO: Arquivo sum_par não existe!\e[0m"
    # [ -f /opt/poisson ] && echo "\e[31mArquivo poisson existe!\e[0m" || echo "\e[31m\aERRO: Arquivo poisson não existe!\e[0m"
