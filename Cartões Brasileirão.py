#!/usr/bin/env python
# coding: utf-8

# # Cartões do Brasileirão

# ## Analisando Banco de dados

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('Arquivos/campeonato-brasileiro-cartoes.csv')


# In[3]:


dados.rename(columns = {'rodata':'rodada'}, inplace = True)


# In[4]:


dados.head(10)


# In[5]:


print(dados.cartao.value_counts()['Amarelo'], 'amarelos') # Vermelhos e Amarelos
print(dados.cartao.value_counts()['Vermelho'], 'vermelhos') 
print(len(dados.cartao), 'cartões no total')


# In[6]:


dados.posicao.unique()


# In[7]:


dados.posicao.fillna('Reserva', inplace = True) # Renomeando o nan para Reserva


# In[8]:


zagueira = dados['posicao'] == 'Zagueira' # Identificando o erro de digitação zagueira
dados[zagueira].head()


# In[9]:


dados['posicao'] = dados['posicao'].replace({'Zagueira' : 'Zagueiro'}) # Tratando de zagueira para zagueiro


# In[10]:


dados.posicao.unique() # Conferindo se o erro foi consertado


# ## Analisando jogadores

# In[11]:


dados.atleta.value_counts() # Quantos cartões cada jogador levou


# In[12]:


vermelho = dados.query('cartao == "Vermelho"') # Separando entre vermelho e amarelo
amarelo = dados.query('cartao == "Amarelo"')


# In[13]:


amarelo['atleta'].value_counts().head() # Números de cartões amarelos levados por cada jogador


# In[14]:


vermelho['atleta'].value_counts().head() # Números de cartões vermelhos levados por cada jogador


# In[15]:


atletas = list(dados.atleta.unique())
d = {'Cartão amarelo' : amarelo['atleta'].value_counts(), # Criando DataFrame de cartões amarelos e vermelhos
     'Cartão vermelho' : vermelho['atleta'].value_counts(),
    }


# In[16]:


df = pd.DataFrame(data = d, index = atletas)
df.fillna(0)


# In[17]:


df.loc[df['Cartão amarelo'].idxmax()]


# In[18]:


flamengo = dados.query('clube == "Flamengo"')


# In[20]:


flamengo['cartao'].value_counts() # Número de cartões levados por jogadores do Flamengo


# In[ ]:




