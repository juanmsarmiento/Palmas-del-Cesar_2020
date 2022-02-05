#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Idea, hacer una encuesta llenando todos los campos para ver que los tome todos
import re
def get_1(txt):
    pat = ",,Edad: ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_2(txt):
    pat = ",Municipio de Nacimiento: ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_3(txt):
    pat = ",Departamento de Nacimiento:,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_5(txt):
    pat = "del cultivo:,(.*?)(?:.?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_7(txt):
    pat = ",,Edad,(.*)"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_8(txt):
    pat = ",3. Ocupación de esposa \(o\) o compañero \(o\) permanente:,,(.*?),," 
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_9(txt):
    pat = ",3. Ocupación de esposa \(o\) o compañero \(o\) permanente:,,(?:.*?),,Otra\? Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_10(txt):
    pat = ",4. Número de personas que conforman su núcleo familiar: ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_11(txt):
    pat = ",5. Cuántos hijos tiene:,,Mujeres \(Cuántos\),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_12(txt):
    pat = ",5. Cuántos hijos tiene:,,Mujeres \(Cuántos\),(?:.*?),Hombres \(Cuántos\),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_13(txt):
    pat = ",6. \¿Tiene hijos con discapacidad o condición especial\? ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_14(txt):
    pat = ",6. \¿Tiene hijos con discapacidad o condición especial\? ,,(?:.*?),\¿Cuántos\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_15(txt):
    pat = '7. Qué tipo de discapacidad tienen:",,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_16(txt):
    pat = ",,,Hijo 1,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_17(txt):
    pat = ",,,Hijo 2,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_18(txt):
    pat = ",,,Hijo 3,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_19(txt):
    pat = ",,,Hijo 4,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_20(txt):
    pat = ",,,Hijo 5,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_21(txt):
    pat = ",,,Hijo 6,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_22(txt):
    pat = ",,,Hijo 1,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_23(txt):
    pat = ",,,Hijo 2,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_24(txt):
    pat = ",,,Hijo 3,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_25(txt):
    pat = ",,,Hijo 4,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_26(txt):
    pat = ",,,Hijo 5,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_27(txt):
    pat = ",,,Hijo 6,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_28(txt):
    pat = ",,,No aplica,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_29(txt):
    pat = ",,,No aplica,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_30(txt):
    pat = ",9. Estado civil de sus hijos: ,,No sabe/no aplica,\¿Cuantos\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_31(txt):
    pat = ",,,Casado,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_32(txt):
    pat = ",,,Unión libre,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_33(txt):
    pat = ",,,Soltero ,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_34(txt):
    pat = ",,,Separado ,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_35(txt):
    pat = ",,,Otro,\¿Cuál\?,(.*?),\n"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_36(txt):
    pat = ",10. Cuantos de sus hijos viven con usted:,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_37(txt):
    pat = ",11. Cuantos de sus hijos tienen su propia familia:,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_38(txt):
    pat = ",12. Cuantas personas conforman el núcleo familiar de sus hijos que tienen su propia familia:  ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_39(txt):
    pat = ",,,Desempleado,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_40(txt):
    pat = ",,,Empleo Formal ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_41(txt):
    pat = ",,,Empleo Informal,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_42(txt):
    pat = ",,,Desempleado,,(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_43(txt):
    pat = ",,,Empleo Formal ,,(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_44(txt):
    pat = ",,,Empleo Informal,,(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_45(txt):
    pat = " permanente ,,Propietario \(a\),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_46(txt):
    pat = " permanente ,,Propietario \(a\),(?:.*?),Esposa,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_47(txt):
    pat = ",,Primaria ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_48(txt):
    pat = ",,Primaria ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_49(txt):
    pat = ",,Secundaria ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_50(txt):
    pat = ",,Secundaria ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_51(txt):
    pat = ",,Técnica,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_52(txt):
    pat = ",,Técnica,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_53(txt):
    pat = ",,Tecnólogo ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_54(txt):
    pat = ",,Tecnólogo ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_55(txt):
    pat = ",,Universitario ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_56(txt):
    pat = ",,Universitario ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_57(txt):
    pat = ",,Posgrado,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_58(txt):
    pat = ",,Posgrado,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_59(txt):
    pat = ",,Primaria ,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_60(txt):
    pat = ",,Primaria ,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_61(txt):
    pat = ",,Secundaria ,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_62(txt):
    pat = ",,Secundaria ,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_63(txt):
    pat = ",,Técnica,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_64(txt):
    pat = ",,Técnica,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_65(txt):
    pat = ",,Tecnólogo ,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_66(txt):
    pat = ",,Tecnólogo ,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_67(txt):
    pat = ",,Universitario ,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_68(txt):
    pat = ",,Universitario ,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_69(txt):
    pat = ",,Posgrado,(?:.*?),(?:.*?),(?:.*?),(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_70(txt):
    pat = ",,Posgrado,(?:.*?),(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_71(txt):
    pat = ",16. Cuantos de los miembros de la familia tienen Seguridad Social: ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_72(txt):
    pat = ",17. Tipo de régimen de seguridad social que usted tiene \(selección múltiple\) Marque X,,Subsidiado,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_73(txt):
    pat = ", Contributivo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_74(txt):
    pat = ",18. A quiénes de la familia los incluye en la seguridad social con régimen contributivo: Marque X,,(.*?),Solo usted"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_75(txt):
    pat = ',18. A quiénes de la familia los incluye en la seguridad social con régimen contributivo: Marque X,,(?:.*?),Solo usted,(.*?),Mamá\s'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_76(txt):
    pat = ",,,(.*?),Esposa \(o\) ,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_77(txt):
    pat = ",,,(?:.*?),Esposa \(o\) ,(.*?), Papá"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_78(txt):
    pat = ",,,(.*?),Hijos,\¿Cuantos\?"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_79(txt):
    pat = ",Hijos,\¿Cuantos\?,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
#Hasta aquí, está recolentando tanto para contributivo como para subsidiado: 0 y par contributivo; impart subisdiado (Revisar)
def get_81(txt):
    pat = ",19. A quiénes de la familia los incluye en la seguridad social con régimen subsidiado  ,,(.*?),Solo usted,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_82(txt):
    pat = ',19. A quiénes de la familia los incluye en la seguridad social con régimen subsidiado  ,,(?:.*?),Solo usted,(.*?),Mamá\s'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_83(txt):
    pat = ",20. Tiene vivienda propia ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_84(txt):
    pat = ",\¿Dónde vive\? ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_85(txt):
    pat = ",21. La vivienda está completamente construida ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_86(txt):
    pat = ",22. La vivienda cuenta con todos los servicios públicos ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_87(txt):
    pat = ",Cuales le faltan  ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_88(txt):
    pat = ",No aplica/no sabe,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_89(txt):
    pat = ",Temas relacionados con el cultivo de palma,Aspectos agronómicos del cultivo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_90(txt):
    pat = ",,Aspectos financieros y de costos del cultivo ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_91(txt):
    pat = ",,Aspectos administrativos del cultivo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_92(txt):
    pat = ",,Aspectos ambientales y de calidad,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_93(txt):
    pat = ",,Aspectos de seguridad y salud en el trabajo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_94(txt):
    pat = ",Cursos relacionados con un hobbies o afición,Deportes,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_95(txt):
    pat = ",,Manualidades,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_96(txt):
    pat = ",,Arte y música,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_97(txt):
    pat = ",,Emprendimiento,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_98(txt):
    pat = ",,Lengua extranjera ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_99(txt):
    pat = ",,Gastronomía ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_101(txt):
    pat = ",Educación formal ,Primaria,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_102(txt):
    pat = ",,Secundaria,(.*?),(?:.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_103(txt):
    pat = ",,Técnico,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_104(txt):
    pat = ",,Tecnólogo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_105(txt):
    pat = ",,Universitario,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_106(txt):
    pat = ",,Posgrado ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_107(txt):
    pat = ",No aplica/no sabe,,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_108(txt):
    pat = ",Temas relacionados con el cultivo de palma,Aspectos agronómicos del cultivo,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_109(txt):
    pat = ",,Aspectos financieros y de costos del cultivo ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_110(txt):
    pat = ",,Aspectos administrativos del cultivo,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_111(txt):
    pat = ",,Aspectos ambientales y de calidad,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_112(txt):
    pat = ",,Aspectos de seguridad y salud en el trabajo,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_113(txt):
    pat = ",Cursos relacionados con un hobbies o afición,Deportes,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_114(txt):
    pat = ",,Manualidades,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_115(txt):
    pat = ",,Arte y música,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_116(txt):
    pat = ",,Emprendimiento,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_117(txt):
    pat = ",,Lengua extranjera ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_118(txt):
    pat = ",,Gastronomía ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_120(txt):
    pat = ",Educación formal ,Primaria,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_121(txt):
    pat = ",,Secundaria,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_122(txt):
    pat = ",,Técnico,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_123(txt):
    pat = ",,Tecnólogo,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_124(txt):
    pat = ",,Universitario,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_125(txt):
    pat = ",,Posgrado ,(?:.*?),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_126(txt):
    pat = ",No aplica/no sabe,,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_127(txt):
    pat = ",Temas relacionados con el cultivo de palma,Aspectos agronómicos del cultivo,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_128(txt):
    pat = ",,Aspectos financieros y de costos del cultivo ,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_129(txt):
    pat = ",,Aspectos administrativos del cultivo,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_130(txt):
    pat = ",,Aspectos ambientales y de calidad,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_131(txt):
    pat = ",,Aspectos de seguridad y salud en el trabajo,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_132(txt):
    pat = ",Cursos relacionados con un hobbies o afición,Deportes,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_133(txt):
    pat = ",,Manualidades,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_134(txt):
    pat = ",,Arte y música,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_135(txt):
    pat = ",,Emprendimiento,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_136(txt):
    pat = ",,Lengua extranjera ,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_137(txt):
    pat = ",,Gastronomía ,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_139(txt):
    pat = ",Educación formal ,Primaria,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_140(txt):
    pat = ",,Secundaria,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_141(txt):
    pat = ",,Técnico,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_142(txt):
    pat = ",,Tecnólogo,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_143(txt):
    pat = ",,Universitario,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_144(txt):
    pat = ",,Posgrado ,(?:.*?),(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_145(txt):
    pat = ',"24. Pasatiempos, aficiones principales del propietario \(a\) del cultivo \(Marque X\): ",, Deportes,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_146(txt):
    pat = ',"24. Pasatiempos, aficiones principales del propietario \(a\) del cultivo \(Marque X\): ",, Deportes,(?:.*?),\¿Cuál\?,(.*?)\s'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_147(txt):
    pat = ",,,Reunión con los amigos \(fiesta\),(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_148(txt):
    pat = ", Reuniones familiares,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_149(txt):
    pat = ",,,Viajes turismo,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_150(txt):
    pat = ",,Viajes turismo,(?:.*?),Ninguno,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_151(txt):
    pat = ',,,Otro \(Cual\): ,(.*?),,\n,"25.'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_152(txt):
    pat = ',"25. Pasatiempos, aficiones principales de la esposa \(o\) o compañera \(o\) permanente \(Marque X\):",,Cursos de Formación ,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_153(txt):
    pat = ',"25. Pasatiempos, aficiones principales de la esposa \(o\) o compañera \(o\) permanente \(Marque X\):",,Cursos de Formación ,(?:.*?),\¿Cuál\?,(.*?)\s'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_154(txt):
    pat = ",,,Deporte ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_155(txt):
    pat = ",,,Deporte ,(?:.*?),\¿Cuál\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_156(txt):
    pat = ",,,Ver Tv – Escuchar Música,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_157(txt):
    pat = ",Otro \(\¿Cuál\?\): ,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_158(txt):
    pat = ",,,Ninguno,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_159(txt):
    pat = ",,,No sabe/no aplica,(.*?),,\n,26."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
#Esta puede ser una solución para los "otros"
def get_160(txt):
    pat = ',26. Que hacen sus hijos durante el tiempo que no estudian o trabajan \(Marque X\): ,,Deporte ,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_161(txt):
    pat = ',26. Que hacen sus hijos durante el tiempo que no estudian o trabajan \(Marque X\): ,,Deporte ,(?:.*?),\¿Cuál\?,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_162(txt):
    pat = ",,,Cursos de Formación ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_163(txt):
    pat = ",,,Cursos de Formación ,(?:.*?),\¿Cuál\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_164(txt):
    pat = ",,,Juegos ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_165(txt):
    pat = ",Reunión con los amigos ,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_166(txt):
    pat = ",,,No sabe/no aplica,(.*?),Ninguno,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_167(txt):
    pat = ",,,No sabe/no aplica,(?:.*?),Ninguno,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_168(txt):
    pat = ",,,Otro (Cual): ,(.*?),,\s,27."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_169(txt):
    pat = ",27. Usted o su familia han sido víctima de hechos relacionados con el conflicto armando o grupos al margen de la ley ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_170(txt):
    pat = ",27. Usted o su familia han sido víctima de hechos relacionados con el conflicto armando o grupos al margen de la ley ,,(?:.*?),\¿Cuál\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_171(txt):
    pat = ",28. Ha tenido algún conflicto sobre la tenencia legal de su cultivo ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_172(txt):
    pat = ',28. Ha tenido algún conflicto sobre la tenencia legal de su cultivo ,,(?:.*?),"Si lo tuvo y lo solucionó, \¿Cuándo\?",,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_173(txt):
    pat = ",29. Documento de propiedad del cultivo,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_174(txt):
    pat = ",Otro \¿Cuál\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_175(txt):
    pat = ",30. Ha tenido proceso de restitución de tierras \(Ley 1448\),,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_176(txt):
    pat = ',30. Ha tenido proceso de restitución de tierras \(Ley 1448\),,(?:.*?),"Si lo tuvo y lo solucionó, \¿Cuándo\?",,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_177(txt):
    pat = ",31. Cuál era su actividad económica antes de dedicarse al cultivo de palma de aceite \(Marque X\):,,Empleado ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_178(txt):
    pat = ", Agricultura ,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_179(txt):
    pat = ",,,Ganadería-Pecuario,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_180(txt):
    pat = "(?:.*?),Comerciante ,(.*?)\s,,,Otro"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_181(txt):
    pat = ",,,Otro \(Cual\): ,(.*?),,\n,32. "
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_182(txt):
    pat = ",32. Tiene otra actividad económica adicional al cultivo de palma:  ,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_183(txt):
    pat = ",32. Tiene otra actividad económica adicional al cultivo de palma:  ,,(?:.*?),\¿Cuál\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_184(txt):
    pat = ",33. Si su respuesta es no. \¿Le gustaría realizar otra actividad económica diferente a la palmicultura\?,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_185(txt):
    pat = ",33. Si su respuesta es no. \¿Le gustaría realizar otra actividad económica diferente a la palmicultura\?,,(?:.*?),\¿Cuál\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_186(txt):
    pat = ",34. Tiene en su cultivo área disponible para emprender proyectos productivos diferentes al cultivo de palma de aceite,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_187(txt):
    pat = ",34. Tiene en su cultivo área disponible para emprender proyectos productivos diferentes al cultivo de palma de aceite,,(?:.*?),Hectáreas,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_188(txt):
    pat = '\(Marque X\):",,Agricultura ,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_189(txt):
    pat = '\(Marque X\):",,Agricultura ,(?:.*?),\¿Cuál\?,(.*?)\s'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_190(txt):
    pat = ",,,Ganadería,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_191(txt):
    pat = ",,,Ganadería,(?:.*?),Pesca,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_192(txt):
    pat = ",,,Avicultura,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_193(txt):
    pat = ",,,Avicultura,(?:.*?), Porcicultura ,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_194(txt):
    pat = ",,,Otro \(Cual\): ,(.*?),\s,36."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_195(txt):
    pat = ",36. Le gustaría recibir capacitación y formación sobre cualquiera de los proyectos mencionados anteriormente:,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_196(txt):
    pat = ",36. Le gustaría recibir capacitación y formación sobre cualquiera de los proyectos mencionados anteriormente:,,(?:.*?),\¿Cuál\?,,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_197(txt):
    pat = ",37. El cultivo de palma tiene vivienda:,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_198(txt):
    pat = ",38. Tipo de estructura o vivienda en el cultivo de palma:,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_199(txt):
    pat = ",38. Tipo de estructura o vivienda en el cultivo de palma:,,(?:.*?),,Otra\? Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_200(txt):
    pat = ",39. Qué tipo de servicios tiene en el cultivo de palma \(Marque X\):,,Ninguno,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_201(txt):
    pat = ",39. Qué tipo de servicios tiene en el cultivo de palma \(Marque X\):,,Ninguno,(?:.*?),Agua,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_202(txt):
    pat = ",,,Luz,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_203(txt):
    pat = ",,,Luz,(?:.*?),Gas domiciliario,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_204(txt):
    pat = ",,,Pozo séptico,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_205(txt):
    pat = ",,,Pozo séptico,(?:.*?),Otro \(Cual\): ,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_206(txt):
    pat = ",40. La zona donde está ubicado su cultivo de palma cuenta con servicios médicos cercanos,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_207(txt):
    pat = ",40. La zona donde está ubicado su cultivo de palma cuenta con servicios médicos cercanos,,(?:.*?),\¿Dónde\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_208(txt):
    pat = ",41. \¿La zona donde está ubicado su cultivo de palma cuenta con instituciones educativas cercanas\?,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_209(txt):
    pat = ",41. \¿La zona donde está ubicado su cultivo de palma cuenta con instituciones educativas cercanas\?,,(?:.*?),\¿Dónde\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_210(txt):
    pat = ",42. El nivel educativo que ofrecen las instituciones educativas es \(Marque X\):,,Primaria,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_211(txt):
    pat = ",42. El nivel educativo que ofrecen las instituciones educativas es \(Marque X\):,,Primaria,(?:.*?),Secundaria,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_212(txt):
    pat = ",,,Carreras técnixas,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_213(txt):
    pat = ",,,Carreras técnixas,(?:.*?),Otro \(Cual\): ,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_214(txt):
    pat = ",43. La zona donde está ubicado su cultivo de palma cuenta con vías de acceso.,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_215(txt):
    pat = ",44. Las vías de acceso están en:,,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_216(txt):
    pat = ",44. Las vías de acceso están en:,,(?:.*?),,Otra\? Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_217(txt):
    pat = ",45. \¿Qué aspecto en su familia han mejorado después del establecimiento del cultivo de palma\? \(Marque X\),,Ninguno,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_218(txt):
    pat = ",45. \¿Qué aspecto en su familia han mejorado después del establecimiento del cultivo de palma\? \(Marque X\),,Ninguno,(?:.*?),\¿Por qué\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_219(txt):
    pat = ",,,Alimentación,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_220(txt):
    pat = ",,,Alimentación,(?:.*?),Educación,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_221(txt):
    pat = ",,,Vivienda,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_222(txt):
    pat = ",,,Vivienda,(?:.*?),Salud,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_223(txt):
    pat = ",,,Otro \(Cual\): ,(.*?)\s,46."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_224(txt):
    pat = ",46. Tiene gerente y/o administrador en el cultivo de palma:,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_225(txt):
    pat = ",46. Tiene gerente y/o administrador en el cultivo de palma:,,(?:.*?),\¿Cuál\?,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_227(txt):
    pat = ",48. Cuantos empleos se generan en el cultivo de palma: ,,Ninguno,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_228(txt):
    pat = ",,,Directos,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_229(txt):
    pat = ",,,Indirectos,\¿Cuantos\?,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_230(txt):
    pat = ",49. Tipo de vinculación de sus empleados:,,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_231(txt):
    pat = ",49. Tipo de vinculación de sus empleados:,,(?:.*?),,Otro\? Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_232(txt):
    pat = ",50. El cultivo de palma ya le está generando ingresos:,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_234(txt):
    pat = ',"51. Como está asumiendo la inversión, costos y gastos del cultivo:",,(.*?),,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_235(txt):
    pat = ',"51. Como está asumiendo la inversión, costos y gastos del cultivo:",,(?:.*?),,Otro\? Cual\?,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_236(txt):
    pat = ",52. Usted y su familia dependen económicamente del cultivo de palma:,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_237(txt):
    pat = ",53. Como invierte los ingresos generados en el cultivo de palma:,,Cultivo de la palma ,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_238(txt):
    pat = ",,,Gastos Familiares ,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_239(txt):
    pat = ",,,Ahorro,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_240(txt):
    pat = ",,,Otros negocios ,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_241(txt):
    pat = ",,,\¿Cuál\?,(.*?),,\s,54. "
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_242(txt):
    pat = ",54. \¿Conoce usted los costos totales de operación de su cultivo de palma\?,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_243(txt):
    pat = ",54. \¿Conoce usted los costos totales de operación de su cultivo de palma\?,,(?:.*?),\¿Cuál es el costo\? ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_244(txt):
    pat = ',"55. Como planifica la inversión, los costos y gastos para el mantenimiento del cultivo :",,Siembra,%,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_245(txt):
    pat = ",,,Mantenimiento de cultivo e infraestructura,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_246(txt):
    pat = ",,,Fertilización,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_247(txt):
    pat = ",,,Sanidad,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_248(txt):
    pat = ",,,Gastos administrativos,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_249(txt):
    pat = ",,,Gastos de cosecha,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_250(txt):
    pat = ",,,Otros,%,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_251(txt):
    pat = ",56. Está interesado \(a\) usted o su familia a continuar y renovar el cultivo de palma,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_252(txt):
    pat = ",56. Está interesado \(a\) usted o su familia a continuar y renovar el cultivo de palma,,(?:.*?),Porque ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_253(txt):
    pat = ",,,Parentesco:(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_254(txt):
    pat = ",,,Parentesco:(?:.*?),Porque ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_255(txt):
    pat = ",57. \¿Qué es lo que más le preocupa del sector palmicultor\?,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_256(txt):
    pat = ",57. \¿Qué es lo que más le preocupa del sector palmicultor\?,,(?:.*?),,Otra\? Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_257(txt):
    pat = ",58. \¿Cuál es la mayor dificultad que tiene o ha tenido en el manejo de su cultivo\? ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_258(txt):
    pat = ",59. Considera que los servicios de asistencia técnica ofrecidos por Palmas del Cesar para el manejo de su cultivo son: ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_259(txt):
    pat = ",60. Qué servicios adicionales a los actuales espera recibir de Palmas del Cesar: ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_260(txt):
    pat = ",61. El cultivo de palma de aceite está cumpliendo las necesidades y expectativas que usted tenía de este negocio,,(.*?),,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_261(txt):
    pat = ",61. El cultivo de palma de aceite está cumpliendo las necesidades y expectativas que usted tenía de este negocio,,(?:.*?),,Porque,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_262(txt):
    pat = ',"62. Quien es la\(s\) persona \(s\) claves a quien consulta para la toma de decisiones estratégicas en su cultivo \(crecimientos futuros, endeudamiento, otros\) \(Marque X\)",,Ninguno,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_263(txt):
    pat = ',"62. Quien es la\(s\) persona \(s\) claves a quien consulta para la toma de decisiones estratégicas en su cultivo \(crecimientos futuros, endeudamiento, otros\) \(Marque X\)",,Ninguno,(?:.*?),Familia,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_264(txt):
    pat = ",,,Socios,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_265(txt):
    pat = ",,,Socios,(?:.*?),Agrónomo propio,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_266(txt):
    pat = ",,,Asesores técnicos palmas del cesar,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_267(txt):
    pat = ",,,Asesores técnicos palmas del cesar,(?:.*?),Personal administrativos de la USP,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_268(txt):
    pat = ",,,Directivos de palmas del cesar,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_269(txt):
    pat = ",,,Directivos de palmas del cesar,(?:.*?),,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_270(txt):
    pat = ",,,Líder de la región,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_271(txt):
    pat = ",,,Líder de la región,(?:.*?),Cual\?,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_272(txt):
    pat = ",,,Líder de la región,(?:.*?),Cual\?,(?:.*?)\s,,,Asociación o gremio,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_273(txt):
    pat = ",,,Líder de la región,(?:.*?),Cual\?,(?:.*?)\s,,,Asociación o gremio,(?:.*?),Cual\?,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_274(txt):
    pat = ",,,Líder de la región,(?:.*?),Cual\?,(?:.*?)\s,,,Asociación o gremio,(?:.*?),Cual\?,(?:.*?)\s,,,Otros,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_275(txt):
    pat = ",,,Otros,(?:.*?),Cual\?,(.*?)\s,63. "
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_276(txt):
    pat = ",63. Nombre las personas o entidades con quien más se relaciona en lo referente al cultivo \(Marque X\),,Proveedores,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_277(txt):
    pat = ",63. Nombre las personas o entidades con quien más se relaciona en lo referente al cultivo \(Marque X\),,Proveedores,(?:.*?),Palmas del César,(.*?)\s"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_278(txt):
    pat = ",,,Entes de control regional o nacional ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_279(txt):
    pat = ",,,Entes de control regional o nacional ,(?:.*?),Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_280(txt):
    pat = ",,,Entes de control regional o nacional ,(?:.*?),Cual\?,(?:.*?)\s,,,Asociación o gremio,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_281(txt):
    pat = ",,,Entes de control regional o nacional ,(?:.*?),Cual\?,(?:.*?)\s,,,Asociación o gremio,(?:.*?),Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_282(txt):
    pat = ",,,Otros,(.*?),Cual\?,(?:.*?)\s,64."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_283(txt):
    pat = ",,,Otros,(?:.*?),Cual\?,(.*?)\s,64."
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_284(txt):
    pat = ",64. Se considera usted como un productor referente en la zona,,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_285(txt):
    pat = ",64. Se considera usted como un productor referente en la zona,,(?:.*?),Porque ,,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_286(txt):
    pat = ",65. Qué dificultades ha tenido como proveedor de palmas de Cesar S.A: ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_287(txt):
    pat = ",66. Cuáles son sus necesidades y expectativas actuales y futuras en la relación comercial con Palmas de Cesar S.A ,,(.*?),,,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_288(txt):
    pat = ',"67. Usted forma parte de una asociación, cooperativa o gremio ",,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_289(txt):
    pat = ',"67. Usted forma parte de una asociación, cooperativa o gremio ",,(?:.*?),Cual\?,,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_290(txt):
    pat = ',"68. Cuál es su participación en esta asociación, cooperativa o miembro \(Marque X\)",,Miembro con voz y voto,(.*?),'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_291(txt):
    pat = ',"68. Cuál es su participación en esta asociación, cooperativa o miembro \(Marque X\)",,Miembro con voz y voto,(?:.*?),Miembro con voz,(.*?)\s,'
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_292(txt):
    pat = ",,,Miembro de junta directiva   ,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_293(txt):
    pat = ",,,Miembro de junta directiva   ,(?:.*?),Cual\?,(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_294(txt):
    pat = ",,,Miembro de junta directiva   ,(?:.*?),Cual\?,(?:.*?)\s,,,Otros,(.*?),"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list
def get_295(txt):
    pat = ",,,Miembro de junta directiva   ,(?:.*?),Cual\?,(?:.*?)\s,,,Otros,(?:.*?),Cual\?(.*?)\s,"
    with open(txt) as txt:
        aux_list = re.findall(pat, str(txt.read()))
    return aux_list


# In[ ]:




