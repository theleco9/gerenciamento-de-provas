#passos:
# 1 gerar a interface de usuarios
# 2 interface com as tarefas de cada um
# 3 interface registrar novas tarefas 
# 4 interface de completamento de tarefas
import pandas as pd
import streamlit as st
tarefas = pd.read_csv("tarefas.csv", skipinitialspace=True)
# 1
st.title(" Gerenciamento de Provas/Projetos/Tarefas")
Materia = st.selectbox("Selecione a matéria", ["Matemática", "Português", "Ciências", "História", "Inglês", "Artes", "Educação Física"])
if Materia == "Matemática":
    st.write("Você selecionou Matemática. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['matematica'] == 'prova', 'matematica'].count(), "prova")
    st.write (tarefas.loc[tarefas['matematica'] == 'tarefa', 'matematica'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['matematica'] == 'projeto', 'matematica'].count(), "projeto")

if Materia == "Português":
    st.write("Você selecionou Português. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['portugues'] == 'prova', 'portugues'].count(), "prova")
    st.write (tarefas.loc[tarefas['portugues'] == 'tarefa', 'portugues'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['portugues'] == 'projeto', 'portugues'].count(), "projeto")

if Materia == "Ciências":
    st.write("Você selecionou Ciências. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['ciencias'] == 'prova', 'ciencias'].count(), "prova")
    st.write (tarefas.loc[tarefas['ciencias'] == 'tarefa', 'ciencias'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['ciencias'] == 'projeto', 'ciencias'].count(), "projeto")

if Materia == "História":
    st.write("Você selecionou História. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['historia'] == 'prova', 'historia'].count(), "prova")
    st.write (tarefas.loc[tarefas['historia'] == 'tarefa', 'historia'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['historia'] == 'projeto', 'historia'].count(), "projeto")

if Materia == "Inglês":
    st.write("Você selecionou Inglês. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['ingles'] == 'prova', 'ingles'].count(), "prova")
    st.write (tarefas.loc[tarefas['ingles'] == 'tarefa', 'ingles'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['ingles'] == 'projeto', 'ingles'].count(), "projeto")

if Materia == "Artes":
    st.write("Você selecionou Artes. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['artes'] == 'prova', 'artes'].count(), "prova")
    st.write (tarefas.loc[tarefas['artes'] == 'tarefa', 'artes'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['artes'] == 'projeto', 'artes'].count(), "projeto")

if Materia == "Educação Física":
    st.write("Você selecionou Educação Física. Aqui estão as tarefas relacionadas a esta matéria.")
    st.write (tarefas.loc[tarefas['educacao_fisica'] == 'prova', 'educacao_fisica'].count(), "prova")
    st.write (tarefas.loc[tarefas['educacao_fisica'] == 'tarefa', 'educacao_fisica'].count(), "tarefa")
    st.write (tarefas.loc[tarefas['educacao_fisica'] == 'projeto', 'educacao_fisica'].count(), "projeto")

# 2
st.sidebar.header("Registrar Nova Tarefa")
nova_tarefa = st.sidebar.selectbox("Selecione o tipo de tarefa", ["prova", "tarefa", "projeto"]) 
nova_materia = st.sidebar.selectbox("Selecione a matéria para a nova tarefa", ["Matemática", "Português", "Ciências", "História", "Inglês", "Artes", "Educação Física"])
if st.sidebar.button("Registrar"):
    if nova_tarefa and nova_materia:
        # Adicionar a nova tarefa ao DataFrame
        if nova_materia == "Matemática":
            tarefas.loc[len(tarefas)] = [nova_tarefa, '', '', '', '', '', '', '']
        elif nova_materia == "Português":
            tarefas.loc[len(tarefas)] = ['', nova_tarefa, '', '', '', '', '', '']
        elif nova_materia == "Ciências":
            tarefas.loc[len(tarefas)] = ['', '', nova_tarefa, '', '', '', '', '']
        elif nova_materia == "História":
            tarefas.loc[len(tarefas)] = ['', '', '', nova_tarefa, '', '', '', '']
        elif nova_materia == "Inglês":
            tarefas.loc[len(tarefas)] = ['', '', '', '', nova_tarefa, '', '', '']
        elif nova_materia == "Artes":
            tarefas.loc[len(tarefas)] = ['', '', '', '', '', nova_tarefa, '', '']
        elif nova_materia == "Educação Física":
            tarefas.loc[len(tarefas)] = ['', '', '', '', '', '', nova_tarefa, '']

        # Salvar o DataFrame atualizado no arquivo CSV
        tarefas.to_csv("tarefas.csv", index=False)
        st.success(f"A tarefa '{nova_tarefa}' para a matéria '{nova_materia}' foi registrada com sucesso! por favor, atualize a página para ver as alterações.")
    else:
        st.error("Por favor, selecione uma tarefa e uma matéria antes de registrar.")

apagar_tarefa = st.sidebar.selectbox("Selecione a tarefa que deseja apagar", ["prova", "tarefa", "projeto"])
apagar_materia = st.sidebar.selectbox("Selecione a matéria da tarefa que deseja apagar", ["Matemática", "Português", "Ciências", "História", "Inglês", "Artes", "Educação Física"])
if st.sidebar.button("Apagar"):
    if apagar_tarefa and apagar_materia:
        # Apagar a tarefa do DataFrame
        if apagar_materia == "Matemática":
            tarefas.loc[tarefas['matematica'] == apagar_tarefa, 'matematica'] = ''
        elif apagar_materia == "Português":
            tarefas.loc[tarefas['portugues'] == apagar_tarefa, 'portugues'] = ''
        elif apagar_materia == "Ciências":
            tarefas.loc[tarefas['ciencias'] == apagar_tarefa, 'ciencias'] = ''
        elif apagar_materia == "História":
            tarefas.loc[tarefas['historia'] == apagar_tarefa, 'historia'] = ''
        elif apagar_materia == "Inglês":
            tarefas.loc[tarefas['ingles'] == apagar_tarefa, 'ingles'] = ''
        elif apagar_materia == "Artes":
            tarefas.loc[tarefas['artes'] == apagar_tarefa, 'artes'] = ''
        elif apagar_materia == "Educação Física":
            tarefas.loc[tarefas['educacao_fisica'] == apagar_tarefa, 'educacao_fisica'] = ''

        # Salvar o DataFrame atualizado no arquivo CSV
        tarefas.to_csv("tarefas.csv", index=False)
        st.success(f"A tarefa '{apagar_tarefa}' para a matéria '{apagar_materia}' foi apagada com sucesso! por favor, atualize a página para ver as alterações.")
    else:
        st.error("Por favor, selecione uma tarefa e uma matéria antes de apagar.")

st.title(" Feito por: Theo Padua")