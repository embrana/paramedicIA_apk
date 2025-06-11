# Instrucciones para compilar ParamedicIA en Android

Este documento contiene las instrucciones para compilar la aplicación ParamedicIA como APK para Android.

## Requisitos previos

- [Node.js](https://nodejs.org/) (versión 20.0.0 o superior)
- [Android Studio](https://developer.android.com/studio) con Android SDK instalado
- [JDK 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) o superior

## Pasos para compilar

### 1. Preparar el entorno

1. Descomprime el archivo ZIP en una carpeta de tu elección
2. Abre una terminal y navega hasta la carpeta donde descomprimiste el archivo

### 2. Instalar dependencias

```bash
npm install
```

### 3. Compilar el frontend

```bash
npm run build
```

### 4. Sincronizar con Capacitor

```bash
npx cap sync
```

### 5. Compilar el APK

#### Opción 1: Usando Android Studio (Recomendado)

1. Abre Android Studio
2. Selecciona "Open an existing Android Studio project"
3. Navega hasta la carpeta donde descomprimiste el archivo y selecciona la carpeta "android"
4. Espera a que Android Studio indexe el proyecto
5. Selecciona "Build > Build Bundle(s) / APK(s) > Build APK(s)"
6. El APK generado estará disponible en `android/app/build/outputs/apk/debug/app-debug.apk`

#### Opción 2: Usando línea de comandos

```bash
cd android
./gradlew assembleDebug
```

El APK generado estará disponible en `android/app/build/outputs/apk/debug/app-debug.apk`

## Configuración realizada

El proyecto ya está configurado con:

1. **Permisos de micrófono y audio**: Se han añadido los permisos necesarios en el AndroidManifest.xml
2. **Integración con Capacitor**: Se ha configurado Capacitor para Android
3. **Clave de OpenAI**: La clave de API de OpenAI ya está configurada en el archivo .env
4. **Acceso al micrófono y reproducción de audio**: El código ya implementa el acceso al micrófono y la reproducción de audio usando la API web estándar

## Solución de problemas

### Error de SDK no encontrado

Si encuentras un error como "SDK location not found", asegúrate de que:

1. Android Studio está instalado correctamente
2. El archivo `local.properties` en la carpeta `android` contiene la ruta correcta a tu SDK de Android:

```
sdk.dir=/ruta/a/tu/android/sdk
```

En Windows, la ruta suele ser algo como:
```
sdk.dir=C\:\\Users\\TuUsuario\\AppData\\Local\\Android\\Sdk
```

En macOS:
```
sdk.dir=/Users/TuUsuario/Library/Android/sdk
```

En Linux:
```
sdk.dir=/home/TuUsuario/Android/Sdk
```

### Error de JDK no encontrado

Asegúrate de tener instalado JDK 17 o superior y que la variable de entorno JAVA_HOME esté configurada correctamente.

## Funcionalidades implementadas

La aplicación ParamedicIA incluye:

1. **Reconocimiento de voz**: Permite al usuario hablar directamente a la aplicación
2. **Reproducción de audio**: Reproduce respuestas de audio generadas por el backend
3. **Interfaz de chat**: Interfaz amigable para consultas médicas de emergencia
4. **Integración con OpenAI**: Utiliza la API de OpenAI para generar respuestas precisas

## Notas adicionales

- La aplicación está configurada para usar la URL del backend: `https://paramedicIA-api.onrender.com`
- Si necesitas cambiar la URL del backend, modifica el archivo `.env` antes de compilar
