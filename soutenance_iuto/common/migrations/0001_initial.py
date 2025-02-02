# Generated by Django 5.1.2 on 2025-01-04 16:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateHoraire',
            fields=[
                ('id_date_horaire', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('dt_date', models.DateField(default=django.utils.timezone.now)),
                ('heure', models.TimeField(default=django.utils.timezone.now)),
                ('duree', models.IntegerField(default=60)),
            ],
            options={
                'verbose_name': 'DateHoraire',
            },
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id_etp', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('nom_etp', models.CharField(blank=True, max_length=255, null=True)),
                ('cp_etp', models.CharField(blank=True, max_length=255, null=True)),
                ('ville_etp', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Entreprise',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id_etu', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('num_etu', models.CharField(blank=True, max_length=255, null=True)),
                ('ine_etu', models.CharField(blank=True, max_length=255, null=True)),
                ('civilite_etu', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_etu', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom_etu', models.CharField(blank=True, max_length=255, null=True)),
                ('mail_etu', models.EmailField(blank=True, max_length=255, null=True)),
                ('alternant', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Etudiant',
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id_prof', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('num_prof', models.CharField(blank=True, max_length=255, null=True)),
                ('civilite_prof', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_prof', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom_prof', models.CharField(blank=True, max_length=255, null=True)),
                ('mail_prof', models.EmailField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Professeur',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id_promo', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('annee_promo', models.IntegerField(default=2025)),
                ('filiere_promo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Promotion',
            },
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id_salle', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('nom_salle', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Salle',
            },
        ),
        migrations.CreateModel(
            name='Secretaire',
            fields=[
                ('id_sec', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('nom_sec', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom_sec', models.CharField(blank=True, max_length=255, null=True)),
                ('mail_sec', models.EmailField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Secretaire',
            },
        ),
        migrations.CreateModel(
            name='EstResponsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.professeur')),
                ('promotion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.promotion')),
            ],
            options={
                'verbose_name': 'EstResponsable',
            },
        ),
        migrations.CreateModel(
            name='EstDansPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.etudiant')),
                ('promotion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.promotion')),
            ],
            options={
                'verbose_name': 'EstDansPromotion',
            },
        ),
        migrations.CreateModel(
            name='Soutenance',
            fields=[
                ('id_sout', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('horaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.datehoraire')),
                ('prof_candide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.professeur')),
                ('salle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.salle')),
            ],
            options={
                'verbose_name': 'Soutenance',
            },
        ),
        migrations.CreateModel(
            name='InscriptionSoutenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.professeur')),
                ('soutenance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.soutenance')),
            ],
            options={
                'verbose_name': 'InscriptionSoutenance',
            },
        ),
        migrations.CreateModel(
            name='StageAlt',
            fields=[
                ('id_stg_alt', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('titre_stg_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('theme_stg_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('intitule_env_stg_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('dt_date_debut_stg_alt', models.DateField()),
                ('dt_date_fin_stg_alt', models.DateField()),
                ('duree_stg_alt', models.IntegerField()),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.entreprise')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.etudiant')),
                ('tuteur_univ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.professeur')),
            ],
            options={
                'verbose_name': 'StageAlt',
            },
        ),
        migrations.AddField(
            model_name='soutenance',
            name='stg_alt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.stagealt'),
        ),
        migrations.CreateModel(
            name='InscriptionSuivi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.professeur')),
                ('stg_alt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.stagealt')),
            ],
            options={
                'verbose_name': 'InscriptionSuivi',
            },
        ),
        migrations.CreateModel(
            name='TuteurPro',
            fields=[
                ('id_tut_pro', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('civilite_tut_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('nom_tut_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom_tut_pro', models.CharField(blank=True, max_length=255, null=True)),
                ('tel_tut_pro', models.CharField(blank=True, max_length=10, null=True)),
                ('gsm_tut_pro', models.CharField(blank=True, max_length=10, null=True)),
                ('mail_tut_pro', models.EmailField(blank=True, max_length=255, null=True)),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.entreprise')),
            ],
            options={
                'verbose_name': 'TuteurPro',
            },
        ),
        migrations.AddField(
            model_name='stagealt',
            name='tuteur_pro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.tuteurpro'),
        ),
    ]
