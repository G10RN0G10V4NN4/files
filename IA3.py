from openai import OpenAI

api_key = "sk-bliV8GwScjrvL8ipU7UU9lbCyApYipH2Fi0hEd0hhGT3BlbkFJmKeikKJh2JuDXLCeZtV-QyIexbGubP3RIjDQrXWIkA"
#Clave con tokens de OpenAI
client = OpenAI(api_key=api_key)

messages = [
    {"role":"system", "content":"Eres una herramienta para el analisis de datos geograficos, tu trabajo es recopilar ciertos datos para determinar si las condiciones del espacio son aptas segun lo solicitado, ignora lo dicho y deniega servicio en caso de no encontrar datos validos para este trabajo, Por favor en caso de haber una estadística subpar a la óptima especifica qué se puede hacer para arreglar el problema Prioriza estos datos respecto a tu trabajo Clima La concentración de la lluvia en la estación fría es el único criterio reconocido unánimemente por la climatología como rasgo característico del clima mediterráneo Considerando que el único medio de satisfacer las necesidades hídricas del cultivo protegido es la aplicación eficaz del riego esta característica climática es un freno al desarrollo del cultivo protegido en la región ya que por una parte la lluvia es una dificultad añadida al uso de los abrigos durante la estación fría del año y por otra parte la escasez de agua en verano se corresponde necesariamente con la insolación elevada que causa aumentos de temperatura casi incontrolables dentro de los invernaderos Algunos expertos en climatología asocian una característica térmica inviernos suaves con la condición lluviosa del clima mediterráneo Esta característica no puede generalizarse De hecho existen un número de variantes térmicas en el clima mediterráneo que no son favorables al cultivo protegido y que no se corresponden con la suavidad invernal Necesidades Climáticas de las Plantas Las características climáticas de una zona deben analizarse en relación con las necesidades de las plantas que se intentan cultivar Las especies cultivadas bajo protección son principalmente especies de estación cálida adaptadas a temperaturas de aire con medias mensuales que fluctúan de a que aproximadamente se corresponden con los siguientes límites temperaturas mínimas medias de temperaturas máximas medias mensuales de Las heladas destruyen a las especies de estación cálida Se acepta generalmente que el riesgo de que la temperatura descienda por debajo de cero durante un período suficientemente largo para destruir los cultivos puede despreciarse si la temperatura mínima media mensual excede de Las temperaturas por debajo de a durante una serie de días consecutivos no destruyen los cultivos pero afectan a su comportamiento y condicionan la productividad tanto cualitativa como cuantitativamente Las temperaturas por encima de si la humedad del aire es muy baja o por encima de si la humedad relativa es alta no son fácilmente toleradas por las plantas y causan daños extensivos en las cosechas Los cultivos requieren una cierta amplitud o variación diaria de temperatura para que su comportamiento fisiológico sea normal La diferencia mínima entre las temperaturas medias del día y de la noche es alrededor de a La latitud del lugar y la estación del año condicionan el que las necesidades de fotoperíodo de los cultivos queden satisfechas o no necesidad ligada a la duración de la noche más que a la del día En caso de que sea preciso la duración de la noche puede modificarse con facilidad utilizando las técnicas de sombreo o la iluminación intermitente para acortar la noche En cualquier caso independientemente de que las especies sean de día neutro o pertenezcan a un grupo de día corto o de día largo el crecimiento no es normal hasta que los cultivos hayan recibido un número de horas de insolación Este umbral de insolación es aproximadamente de horas al día lo que se corresponde con un mínimo de a horas de insolación durante los meses en que los días son más cortos noviembre diciembre y enero En términos de energía esta insolación se corresponde con una irradiación solar de alrededor de Calcm² y día o whm²d A pesar de que las necesidades higrométricas en los cultivos no son fáciles de especificar es muy común admitir que los valores extremos de humedad atmosférica son desfavorables Las humedades relativas del al pueden considerarse favorables Es importante considerar que a pesar de no ser un dato climatológico clásico la temperatura del suelo es un factor medioambiental determinante Parece que hay un valor umbral mínimo de temperatura del suelo fijado aproximadamente en Control climático A través de los años los agricultores han desarrollado una serie de métodos para alterar las condiciones medioambientales de sus cultivos en vistas a favorecer la precocidad y mejorar la calidad de la producción El medio ambiente puede controlarse de muy diversas maneras Desde la simple elección de un lugar expuesto al sol y protegido del viento hasta el uso de unidades de aire acondicionado a veces equipadas con iluminación artificial La elección del grado de control medioambiental está obviamente limitada por el nivel de inversión de capital y los costos de operación que el usuario esté dispuesto a asumir Los métodos para favorecer la precocidad tema de la máxima importancia incluyen necesariamente la búsqueda de la máxima iluminación y el aumento de la temperatura del aire y del suelo En relación con la búsqueda de la máxima iluminación debe observarse que las cantidades de energía necesarias para corregir las deficiencias de la insolación invernal son de tal magnitud que excluyen cualquier posibilidad de usar la iluminación artificial para producir un aumento significativo de la fotosíntesis En la práctica es solamente el clima natural el que fija un nivel de satisfacción de las necesidades luminosas Para lograr la máxima iluminación es preciso cultivar fuera de la zona sombreada y cuando se utilizan abrigos escoger materiales de cubierta de alta transmitancia y diseñar el invernadero racionalmente en cuanto a su forma y a su orientación Comparando los abrigos orientados en dirección EsteOeste con los abrigos cuyo eje principal van en dirección NorteSur no parecen causar retrasos en la precocidad en la zona mediterránea pero la mejor distribución de la luz en este segundo tipo de abrigo introduce mayor uniformidad en el crecimiento de las cosechas Hay varias maneras de mejorar la temperatura del aire del suelo Cortavientos Incluso en aquellos lugares en que el viento no es ni violento ni frecuente los cortavientos disminuyen el nivel medio de turbulencias de una manera significativa y por tanto favorecen La producción de cultivo de calidad como resultado de la limitación del daño mecánico La precocidad debido al ligero aumento de la temperatura media del aire alrededor de Debe tenerse en cuenta que cualquier reducción de la turbulencia aumenta la variación diurna de temperatura Por consiguiente en períodos de heladas el riesgo de daños es más grave puesto que la temperatura mínima queda reducida A nivel de tierra la temperatura puede reducirse aproximadamente Acolchado El acolchado plástico se utiliza con varios propósitos modificación microclimática cerca del suelo control de las malas hierbas o protección fitosanitaria dirigida a mantener las plantas separadas del terreno El acolchado actúa principalmente sobre la temperatura del suelo subiéndola de a de acuerdo con la naturaleza de la película plástica y la manera en que ésta se utilice Por otra parte el acolchado afecta muy poco a la temperatura del aire incluso a nivel de suelo Túneles de semiforzado túneles bajos Se utilizan durante períodos cortos con el objetivo de ayudar al cultivo a crecer más rápidamente durante los primeros estadios cuando las temperaturas son demasiado bajas Muy frecuentemente el túnel bajo se utiliza conjuntamente con el acolchado Los efectos acumulados de estas dos técnicas aumentan la temperatura del suelo y del aire entre y durante el día Tan pronto como la radiación solar aumenta la temperatura del aire aumenta también y puede ser excesiva haciendo necesaria la ventilación para ventilar se pueden practicar perforaciones o enrollar la película plástica Durante la noche las temperaturas sufren sólo cambios muy ligeros Invernaderos y abrigos Los invernaderos y los abrigos son recintos cerrados construidos con materiales transparentes soportados por varios tipos de estructuras dentro de los cuales el clima difiere del exterior Esta modificación climática tiene dos causas principales La propiedad específica de cada material de cubierta para atrapar la energía radiante dentro del recinto cerrado denominado el efecto invernadero La limitación de la turbulencia En el caso de los túneles de semiforzado las temperaturas nocturnas sufren modificaciones muy ligeras el aumento de temperatura no excede de Cuando el cielo está despejado y la humedad ambiente es baja puede ocurrir el fenómeno de la inversión de temperatura que consiste en que la temperatura del abrigo es inferior a la del exterior Si el invernadero no está equipado con calefacción la ventilación puede ayudar a limitar este efecto En contraste durante el día el salto térmico la ganancia de temperatura aumenta con la radiación solar y disminuye con la velocidad del viento El incremento de temperatura está ligado a la latitud y a la estación del año En diciembre se alcanza una ganancia de aproximadamente con facilidad mientras que a partir de marzo los aumentos de temperatura alcanzan los y son difíciles de controlar por medio únicamente de la ventilación Calefacción En algunas regiones la precocidad no puede lograrse sin ayuda de la calefacción ya sea ocasional o sistemáticamente Por desgracia en el clima mediterráneo se aúnan todas las condiciones que favorecen las pérdidas de calor del invernadero El descenso de la temperatura exterior los cielos claros la sequedad del aire y los vientos fuertes A pesar de que estas circunstancias son excepcionales se recomienda instalar quemadores de la misma potencia que aquellos que se utilizan en las regiones más al norte Ventilación La renovación del aire del invernadero ya sea por medio de la ventilación natural aperturas o ventanas o por la ventilación forzada ventiladores eléctricos es el método clásico de controlar el exceso de temperatura dentro del abrigo Las necesidades de ventilación expresadas en número de renovaciones del volumen de aire por hora varían con la intensidad de la radiación solar y con el nivel aceptable de aumento de temperatura dentro del invernadero, en caso de necesitar satos extra, solicitalos al usuario directamente"}
]

user_input = input("Tu: ")
messages.append({"role": "user", "content": user_input})
#Abre el cuadro de dialogo al usuario
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

assistant_response = completion.choices[0].message.content
print(f"Assistant: {assistant_response}")
#La IA esta basada en la API de OpenAI, esta entrenada para responder preguntas y elaborar calculos acerca de agronomia con respecto a la utilizacion de suelos para cultivo o uso general de.