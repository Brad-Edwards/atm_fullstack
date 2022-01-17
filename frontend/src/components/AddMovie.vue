<!--
  AddMovie.vue

  This component displays an add movie form and submits it for 
  addition to the database.
-->
<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="text"
          class="form-control"
          id="title"
          required
          v-model="movie.title"
          name="title"
        />
      </div>

    <div class="form-group">
    <label for="release_year">Release Year</label>
    <input
        type="text"
        class="form-control"
        id="release_year"
        required
        v-model="movie.release_year"
        name="release_year"
    />
    </div>
   
    <div class="form-group">
      <label for="duration">Duration</label>
      <input
          type="text"
          class="form-control"
          id="duration"
          required
          v-model="movie.duration"
          name="duration"
      />
      </div>
      
      <div class="form-group">
        <label for="description">Description</label>
        <input
            class="form-control"
            id="description"
            required
            v-model="movie.description"
            name="description"
        />
        </div> 

      <div class="form-group">
        <label for="poster_uri">Poster URL</label>
        <input
            class="form-control"
            id="poster_uri"
            required
            v-model="movie.poster_uri"
            name="poster_uri"
        />
        </div>

      <button @click="saveMovie" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newMovie">Add</button>
    </div>
  </div>
</template>

<script>
import MovieDataService from "../services/MovieDataService";

export default {
  name: "add-movie",
  data() {
    return {
      movie: {
        id: null,
        title: "",
        description: "",
        release_year: "",
        duration: "",
        poster_uri: "",
      },
      submitted: false
    };
  },
  methods: {
    saveMovie() {
      // Saves a movie to the database.
      this.movie.release_year;
      var data = {
        title: this.movie.title,
        description: this.movie.description,
        release_year: this.movie.release_year,
        duration: this.movie.duration,
        poster_uri: this.movie.poster_uri,
      };

      MovieDataService.create(data)
        .then(response => {
          this.movie.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    newMovie() {
      // Resets the form after a movie is subbmite
      this.submitted = false;
      this.movie = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>