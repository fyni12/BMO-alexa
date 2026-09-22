<script setup>
// Obtenemos la URL de la API desde la configuración
const config = useRuntimeConfig()

// Hacemos la petición al backend de NestJS
const { data: mensaje, pending, error } = await useFetch('/', {
  baseURL: config.public.apiUrl
})
</script>

<template>
  <div style="font-family: sans-serif; padding: 2rem;">
    <h1>Mi Template Nuxt + Nest</h1>
    
    <div v-if="pending">Cargando datos del servidor...</div>
    <div v-else-if="error">Error al conectar con NestJS: {{ error.message }}</div>
    
    <div v-else style="background: #e2e8f0; padding: 1rem; border-radius: 8px;">
      <strong>Respuesta del Backend:</strong> {{ mensaje }}
    </div>
  </div>
</template>