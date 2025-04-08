# ¿Cuántos paneles caben?

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

<aside>
🙂 **¿Qué esperamos?** La idea es simular de la forma más simple y completa una tarea dentro del equipo técnico de Ruuf. El ejercicio está enfocado en desarrollar un algoritmo que reciba inputs, resuelva un problema matemático y entrega la respuesta.

</aside>

---

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones “a” y “b” (paneles solares) que caben dentro de un rectángulo de dimensiones “x” e “y” (techo), según se muestra en la siguiente figura:

![Untitled](https://img.notionusercontent.com/s3/prod-files-secure%2F5fd840ef-599c-4be1-aeef-1ea8a114fce5%2F9dd7880a-77cd-4127-984b-00d26d5549bd%2FUntitled.png/size/w=480?exp=1743826326&sig=M0_nl2lXIaJk-wr7RkqKLNASCWiNU13Xuj_YRbiKudE&id=88757d0e-7edf-4fff-b493-0a4a0025e338&table=block)

Por ejemplo, podríamos decir que en el siguiente ejemplo caben 5 rectángulos de dimensiones 1 y 2, en un rectángulo de dimensiones 3 y 5.

![               ¿O caben más? 👀](https://img.notionusercontent.com/s3/prod-files-secure%2F5fd840ef-599c-4be1-aeef-1ea8a114fce5%2Ff2217992-2d65-47e2-9865-087d5dbbb978%2FUntitled.png/size/w=480?exp=1743826340&sig=EAyYbHAIZSpk5Ee1WdYbHyQYgMaoNOjQhM9Z1fqVVPY&id=8d87b35d-e0ee-4143-b22d-4b07b068cc41&table=block)

               ¿O caben más? 👀

## 📜 Instrucciones

- Usa el lenguaje/framework que más te acomode. No hay una solución única al problema, por lo que puedes hacer lo que prefieras.
- El algoritmo debe ser una sola función que reciba las dimensiones y retorne un solo integer con la cantidad de paneles que caben.
- No hay restricciones de orientación. Pon todos los rectángulos que puedas en la posición y sentido que prefieras.
- No se pide nada gráfico.

## ✅ Algunos ejemplos para que revises tu código:

- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 💰 Bonus Opcional

¿Te pareció demasiado fácil? ¿Te entretuviste y quieres resolver algo un poco más complejo?

Te dejamos dos alternativas que puedes intentar resolver también. Pero ojo que con resolver el problema base bien ya es suficiente para entrar al proceso 🙂 Si haces el bonus, puedes explicarlo o no en el video. Solo recuerda que no debes pasarte de los 3 minutos de duración.

**Opción 1**

Repetir el ejercicio base, considerando un techo triangular, isóceles.

![Untitled](https://img.notionusercontent.com/s3/prod-files-secure%2F5fd840ef-599c-4be1-aeef-1ea8a114fce5%2Fbf1e4651-277b-4a42-b9ea-b59fe177793b%2FUntitled.png/size/w=580?exp=1743826354&sig=WBCkMPy-ruuOCVf_jrkCAu8vTuG-bLc2dZJ9eeQfcp4&id=af2d8d30-8618-48bc-a582-b7ac7e6da677&table=block)

**Opción 2**

Repetir el ejercicio base considerando dos rectángulos iguales superpuestos. Puedes parametrizar la superposición entre ambos rectángulos.

![Untitled](https://img.notionusercontent.com/s3/prod-files-secure%2F5fd840ef-599c-4be1-aeef-1ea8a114fce5%2F2db5592c-1f8d-4fd4-abeb-09f3f856b429%2FUntitled.png/size/w=670?exp=1743826363&sig=IgslTi3Bvg5pv6W32ci2MfADO-tQL1oKnDA_BxeZ1pY&id=716f4de4-88e6-459b-97b3-1f72fbe892f1&table=block)

## 😕 ¿Algo no se entiende o tienes preguntas?

Si tienes dudas del enunciado del problema, te pedimos que tomes tus propios supuestos y después los comentas en el video. No hay problema con eso 😉.

Si tienes dudas por otro motivo, escríbenos a jobs@ruuf.solar y te ayudaremos con cualquier inquietud.