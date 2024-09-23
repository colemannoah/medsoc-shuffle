<template>
  <main>
    <div class="px-4 py-5 my-5 text-center">
      <h1 class="display-5 fw-bold text-body-emphasis">MedSoc Shuffle</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">
          Upload your CSV file from the Google Form and let the magic happen.
        </p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <input
            type="file"
            class="form-control"
            id="inputGroupFile02"
            accept=".csv"
            @change="handleFileUpload"
          />
          <button class="btn btn-primary" type="button" @click="submitFile">Upload</button>
        </div>
        <div v-if="message">{{ message }}</div>
      </div>
    </div>
    <LocationEmailGrid :locationEmailData="locationEmailData" />
  </main>
  <footer class="text-center py-3">
    <p>Powered by machine learning, made with ❤️ by Noah (Aldo can't code)</p>
  </footer>
</template>

<script setup>
import axios from 'axios'
import LocationEmailGrid from '../components/LocationEmailGrid.vue';
</script>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      message: '',
      locationEmailData: {},
    }
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0]
    },
    async submitFile() {
      if (!this.selectedFile) {
        this.message = 'Please select a file to upload'
        return
      }

      const formData = new FormData()
      formData.append('file', this.selectedFile)

      try {
        const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        this.message = response.data.message
        this.locationEmailData = response.data.assignments
      } catch (error) {
        this.message = error.response.data.error || 'Error uploading file'
      }
    }
  }
}
</script>
