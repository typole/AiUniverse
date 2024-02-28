// frontend/src/views/FirstRequest.vue

<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    };
  },
  mounted() {
    this.getFirstRequest();
  },
  methods: {
    async getFirstRequest() {
      try {
        const response = await fetch('/api/first-request/');
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>
