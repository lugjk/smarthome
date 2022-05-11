import { Alert, StyleSheet, Touchable, TouchableOpacity } from "react-native";
import { RootStackScreenProps } from "../types";
import { Text, View } from "../components/Themed";

import {
  Box,
  Heading,
  VStack,
  FormControl,
  Input,
  Button,
  Center,
  Link,
} from "native-base";
import { useState } from "react";
import { IAuth, User } from "../models/models";
import { user } from "../context/userContext";
import { server } from "../config/url";

export default function LoginScreen({
  navigation,
}: RootStackScreenProps<"Login">) {
  const [auth, setAuth] = useState<IAuth>({
    username: "",
    password: "",
  });

  const onSubmit = () => {

    fetch(server+'users/login', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: auth.username,
        password: auth.password
      })
    }).then((response) => {
      if (response.ok) return response.json()
      else if(response.status == 404) throw new Error("Invalid email or password")
    })
      .then((json) => {
        user._id = json.data._id
        user.token = json.data.token
        user.email = json.data.email 
        user.username = json.data.name
        navigation.navigate("AllRoomScreen");
    })
    .catch((error) => {
      alert(error)
    });

    // if (auth.username === "123" && auth.password === "123") {
    //   Alert.alert("Alert Title", "Dang nhap thanh cong", [
    //     { text: "OK", onPress: () => console.log("OK Pressed") },
    //   ]);
    //   navigation.navigate("AllRoomScreen");
    // } else {
    //   Alert.alert("Alert Title", "Dang nhap that bai", [
    //     { text: "OK", onPress: () => console.log("OK Pressed") },
    //   ]);
    //   console.log("Dang nhap that bai", auth);
    // }
  };

  return (
    <View style={styles.container}>
      <Center w="100%">
        <Box safeArea p="2" py="8" w="90%" maxW="290">
          <Heading
            size="lg"
            fontWeight="600"
            color="coolGray.800"
            _dark={{
              color: "warmGray.50",
            }}
          >
            Welcome
          </Heading>
          <Heading
            mt="1"
            _dark={{
              color: "warmGray.200",
            }}
            color="coolGray.600"
            fontWeight="medium"
            size="xs"
          >
            Sign in to continue!
          </Heading>

          <VStack space={3} mt="5">
            <FormControl>
              <FormControl.Label>Username</FormControl.Label>
              <Input
                value={auth.username}
                onChangeText={(value) => {
                  setAuth((prev) => ({
                    ...prev,
                    username: value,
                  }));
                }}
              />
              {/* {!auth.username && <Text>vui long nhap username</Text>} */}
            </FormControl>
            <FormControl>
              <FormControl.Label>Password</FormControl.Label>
              <Input
                type="password"
                value={auth.password}
                onChangeText={(value) => {
                  setAuth((prev) => ({
                    ...prev,
                    password: value,
                  }));
                }}
              />
              {/* <TouchableOpacity
                onPress={() => {
                  navigation.push("IDscreen");
                }}
              >
                <Text>Change Password?</Text>
              </TouchableOpacity> */}
            </FormControl>
                  <Button mt="2" colorScheme="indigo" onPress={onSubmit}>
                    Sign in
                  </Button>

          </VStack>
        </Box>
      </Center>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
  },
  link: {
    marginTop: 15,
    paddingVertical: 15,
  },
  linkText: {
    fontSize: 14,
    color: "#2e78b7",
  },
});
