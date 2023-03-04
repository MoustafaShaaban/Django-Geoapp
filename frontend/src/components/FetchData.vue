<script>
import axios from "axios";

export default {
    data() {
        return {
            features: [],
        }
    },
    methods: {
        fetchData: function () {
            axios
                .get(import.meta.env.VITE_API_ENDPOINT , {
                    auth: {
                        username: "admin",
                        password: "1234"
                    }
                })
                .then(response => (this.features = response.data))
                .catch((error) => {
                    console.error(error);
                })
        },
    },
    mounted() {
        this.fetchData();
    }
}
</script>

<template>
    <h1>Available Features</h1>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Type</th>
                <th scope="col">Description</th>
                <th scope="col">Latitude</th>
                <th scope="col">Longitude</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="feature in features" :key="feature.id">
                <td>{{ feature.name }}</td>
                <td>{{ feature.type }}</td>
                <td>{{ feature.description }}</td>
                <td>{{ feature.latitude }}</td>
                <td>{{ feature.longitude }}</td>
            </tr>
        </tbody>
    </table>
</template>