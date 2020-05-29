# Generated by Django 2.2 on 2020-05-29 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20, unique=True, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=80, verbose_name='Cliente')),
                ('plano', models.CharField(max_length=20, verbose_name='Plano')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=40, verbose_name='Bairro')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Email_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Email_Cliente',
                'verbose_name_plural': 'Email_Clientes',
            },
        ),
        migrations.CreateModel(
            name='Email_fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Email_Fornecedor',
                'verbose_name_plural': 'Email_Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.CharField(max_length=40, unique=True, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(max_length=80, verbose_name='Razão Social.')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('inscricao_estadual', models.CharField(max_length=15, verbose_name='I.Estadual:')),
                ('categoria', models.CharField(choices=[('Material de Limpeza e Higiene', 'Material de Limpeza e Higiene'), ('Material de Copa', 'Material de Copa'), ('Alimentos em Geral', 'Alimentos em Geral'), ('Frutas e Verduras', 'Frutas e Verduras'), ('Material de Escritório', 'Material de Escritório'), ('Bebidas', 'Bebidas'), ('Descartáveis e Embalagens', 'Descartáveis e Embalagens'), ('Itens de Manutenção Básica', 'Itens de Manutenção Básica')], max_length=100)),
                ('cep', models.CharField(max_length=11, verbose_name='CEP')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=30, verbose_name='UF')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('telefone', models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=17, null=True, verbose_name='Celular')),
                ('email', models.CharField(blank=True, max_length=150, null=True, verbose_name='Email')),
                ('observacao', models.CharField(blank=True, max_length=400, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Pedido_de_cotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agora', models.DateTimeField()),
                ('nome', models.CharField(max_length=40, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(max_length=80, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('plano', models.CharField(max_length=1, verbose_name='Tipo do Plano')),
                ('cep', models.CharField(max_length=11, verbose_name='CEP')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('telefone', models.CharField(max_length=16, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=17, verbose_name='Celular')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('produto1', models.CharField(max_length=25, verbose_name='Produto 1')),
                ('categoria1', models.CharField(max_length=100, verbose_name='Categoria 1')),
                ('valor_base1', models.CharField(max_length=9, verbose_name='Valor Base 1')),
                ('unidade_medida1', models.CharField(max_length=9, verbose_name='Unidade de Medida 1')),
                ('quantidade1', models.CharField(max_length=5, verbose_name='Quantidade 1')),
                ('marca1', models.CharField(max_length=9, verbose_name='Marca 1')),
                ('produto2', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 2')),
                ('categoria2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 2')),
                ('valor_base2', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 2')),
                ('unidade_medida2', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 2')),
                ('quantidade2', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 2')),
                ('marca2', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 2')),
                ('produto3', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 3 ')),
                ('categoria3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 3')),
                ('valor_base3', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 3')),
                ('unidade_medida3', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 3')),
                ('quantidade3', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 3')),
                ('marca3', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 3')),
                ('produto4', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 4')),
                ('categoria4', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 4')),
                ('valor_base4', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 4')),
                ('unidade_medida4', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 4')),
                ('quantidade4', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 4')),
                ('marca4', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 4')),
                ('produto5', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 5')),
                ('categoria5', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 5')),
                ('valor_base5', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 5')),
                ('unidade_medida5', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 5')),
                ('quantidade5', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 5')),
                ('marca5', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 5')),
                ('produto6', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 6')),
                ('categoria6', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 6')),
                ('valor_base6', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 6')),
                ('unidade_medida6', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 6')),
                ('quantidade6', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 6')),
                ('marca6', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 6')),
                ('produto7', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 7')),
                ('categoria7', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 7')),
                ('valor_base7', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 7')),
                ('unidade_medida7', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 7')),
                ('quantidade7', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 7')),
                ('marca7', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 7')),
                ('produto8', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 8')),
                ('categoria8', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 8')),
                ('valor_base8', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 8')),
                ('unidade_medida8', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 8')),
                ('quantidade8', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 8')),
                ('marca8', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 8')),
                ('produto9', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 9')),
                ('categoria9', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 9')),
                ('valor_base9', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 9')),
                ('unidade_medida9', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 9')),
                ('quantidade9', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 9')),
                ('marca9', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 9')),
                ('produto10', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 10')),
                ('categoria10', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 10')),
                ('valor_base10', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 10')),
                ('unidade_medida10', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 10')),
                ('quantidade10', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade10')),
                ('marca10', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 10')),
                ('produto11', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 11')),
                ('categoria11', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 11')),
                ('valor_base11', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 11')),
                ('unidade_medida11', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 11')),
                ('quantidade11', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 11')),
                ('marca11', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 11')),
                ('produto12', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 12')),
                ('categoria12', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 12')),
                ('valor_base12', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 12')),
                ('unidade_medida12', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 12')),
                ('quantidade12', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 12')),
                ('marca12', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 12')),
                ('produto13', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 13')),
                ('categoria13', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 13')),
                ('valor_base13', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 13')),
                ('unidade_medida13', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 13')),
                ('quantidade13', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 13')),
                ('marca13', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 13')),
                ('produto14', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 14')),
                ('categoria14', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 14')),
                ('valor_base14', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 14')),
                ('unidade_medida14', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 14')),
                ('quantidade14', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 14')),
                ('marca14', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 14')),
                ('produto15', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 15')),
                ('categoria15', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 15')),
                ('valor_base15', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 15')),
                ('unidade_medida15', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 15')),
                ('quantidade15', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 15')),
                ('marca15', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 15')),
                ('produto16', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 16')),
                ('categoria16', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 16')),
                ('valor_base16', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 16')),
                ('unidade_medida16', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 16')),
                ('quantidade16', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 16')),
                ('marca16', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 16')),
                ('produto17', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 17')),
                ('categoria17', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 17')),
                ('valor_base17', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 17')),
                ('unidade_medida17', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 17')),
                ('quantidade17', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 17')),
                ('marca17', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 17')),
                ('produto18', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 18')),
                ('categoria18', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 18')),
                ('valor_base18', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 18')),
                ('unidade_medida18', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 18')),
                ('quantidade18', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 18')),
                ('marca18', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 18')),
                ('produto19', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 19')),
                ('categoria19', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 19')),
                ('valor_base19', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 19')),
                ('unidade_medida19', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 19')),
                ('quantidade19', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 19')),
                ('marca19', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 19')),
                ('produto20', models.CharField(blank=True, max_length=25, null=True, verbose_name='Produto 20')),
                ('categoria20', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria 20')),
                ('valor_base20', models.CharField(blank=True, max_length=9, null=True, verbose_name='Valor Base 20')),
                ('unidade_medida20', models.CharField(blank=True, max_length=9, null=True, verbose_name='Unidade de Medida 20')),
                ('quantidade20', models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantidade 20')),
                ('marca20', models.CharField(blank=True, max_length=9, null=True, verbose_name='Marca 20')),
            ],
            options={
                'verbose_name': 'Pedido_de_cotacao',
                'verbose_name_plural': 'Pedidos_de_cotacao',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=20, verbose_name='Produto')),
                ('valor_base', models.CharField(max_length=20, verbose_name='Valor Base')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria')),
                ('unidade_medida', models.CharField(max_length=2, verbose_name='Unidade de Medida')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Sala_de_leilao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(max_length=20, verbose_name='Pedido_de_cotacao')),
            ],
            options={
                'verbose_name': 'Sala_de_leilao',
                'verbose_name_plural': 'Salas_de_leilao',
            },
        ),
        migrations.CreateModel(
            name='Email_fornecedor_envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Email_fornecedor')),
            ],
            options={
                'verbose_name': 'Email_fornecedor_envio',
                'verbose_name_plural': 'Email_fornecedor_envio',
            },
        ),
    ]
