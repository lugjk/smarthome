import { Alert, StyleSheet } from "react-native";
import { View } from "../components/Themed";
import { RootStackScreenProps } from "../types";
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
import { IAuth2, IAuth } from "../models/models";

export default function IDscreen({
  navigation,
}: RootStackScreenProps<"IDscreen">) {
  const [changeauth, setAuth] = useState<IAuth2>({
    username: "",
    password: "",
    changepassword: "",
  });

  const onSubmit = () => {
    if (changeauth.username === "123" && changeauth.password === "123") {
      console.log("Successfully  change password", changeauth);
      Alert.alert("Alert Title", "Successfully change password", [
        { text: "OK", onPress: () => console.log("OK Pressed") },
      ]);
    } else {
      Alert.alert("Alert Title", "Change password failed", [
        { text: "OK", onPress: () => console.log("OK Pressed") },
      ]);
      console.log("Change password failed", changeauth);
    }
  };

  return (
    <View style={styles.container}>
      <Center w="100%">
        <Box safeArea p="2" py="8" w="90%" maxW="290">
          <VStack space={3} mt="5">
            <FormControl>
              <FormControl.Label>Username</FormControl.Label>
              <Input
                value={changeauth.username}
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
                value={changeauth.password}
                onChangeText={(value) => {
                  setAuth((prev) => ({
                    ...prev,
                    password: value,
                  }));
                }}
              />
            </FormControl>
            <FormControl>
              <FormControl.Label>Username</FormControl.Label>
              <Input
                value={changeauth.changepassword}
                onChangeText={(value) => {
                  setAuth((prev) => ({
                    ...prev,
                    changepassword: value,
                  }));
                }}
              />
              {/* {!auth.username && <Text>vui long nhap username</Text>} */}
            </FormControl>
            <Button mt="2" colorScheme="indigo" onPress={onSubmit}>
              Change password
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
