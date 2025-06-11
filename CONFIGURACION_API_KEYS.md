# Instrucciones para configurar claves API de forma segura

## Configuración de la clave API de OpenAI

Para que la aplicación ParamedicIA funcione correctamente, necesitas configurar la clave API de OpenAI de forma segura. A continuación, se detallan los pasos para hacerlo tanto en GitHub como localmente.

### Opción 1: Configurar en GitHub Actions (Recomendado)

1. **Crear un repositorio en GitHub**
   - Crea un nuevo repositorio en tu cuenta de GitHub
   - Sube todo el contenido del archivo ZIP a este repositorio

2. **Configurar el Secret en GitHub**
   - Ve a tu repositorio en GitHub
   - Haz clic en "Settings" (Configuración)
   - En el menú lateral, selecciona "Secrets and variables" > "Actions"
   - Haz clic en "New repository secret"
   - Nombre: `OPENAI_API_KEY`
   - Valor: `[INSERTA TU CLAVE API DE OPENAI AQUÍ]`
   - Haz clic en "Add secret"

3. **Ejecutar el workflow**
   - Ve a la pestaña "Actions" en tu repositorio
   - Selecciona el workflow "Build Android APK"
   - Haz clic en "Run workflow"
   - El workflow utilizará automáticamente la clave API configurada como secret

### Opción 2: Configurar localmente

Si prefieres compilar la aplicación en tu entorno local:

1. **Crear archivo .env**
   - En la raíz del proyecto, crea un archivo llamado `.env`
   - Añade la siguiente línea:
   ```
   OPENAI_API_KEY=[INSERTA TU CLAVE API DE OPENAI AQUÍ]
   ```

2. **Asegúrate de no subir el archivo .env a GitHub**
   - El archivo `.gitignore` ya está configurado para excluir el archivo `.env`
   - Verifica que el archivo `.env` no se incluya en tus commits

## Notas importantes sobre seguridad

- **Nunca** incluyas claves API directamente en el código fuente
- **Nunca** subas archivos `.env` con claves API a repositorios públicos
- Utiliza siempre variables de entorno o secrets para manejar información sensible
- Si necesitas compartir el proyecto, asegúrate de eliminar cualquier clave API antes de hacerlo

## Verificación de la configuración

Para verificar que la clave API está correctamente configurada:

1. **En entorno local**:
   - Ejecuta `python test_openai.py` después de configurar el archivo `.env`
   - Deberías ver un mensaje confirmando la conexión exitosa con OpenAI

2. **En GitHub Actions**:
   - Después de ejecutar el workflow, verifica los logs para confirmar que la compilación se completó correctamente
   - Descarga el APK generado y pruébalo en un dispositivo Android
