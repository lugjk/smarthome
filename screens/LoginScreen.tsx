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
import { IAuth } from "../models/models";

export default function LoginScreen({
  navigation,
}: RootStackScreenProps<"Login">) {
  const [auth, setAuth] = useState<IAuth>({
    username: "",
    password: "",
  });

  const onSubmit = () => {
    if (auth.username === "123" && auth.password === "123") {
      console.log("Dang nhap thanh cong", auth);
      Alert.alert("Alert Title", "Dang nhap thanh cong", [
        { text: "OK", onPress: () => console.log("OK Pressed") },
      ]);
      navigation.navigate("AllRoomScreen");
    } else {
      Alert.alert("Alert Title", "Dang nhap that bai", [
        { text: "OK", onPress: () => console.log("OK Pressed") },
      ]);
      console.log("Dang nhap that bai", auth);
    }
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
              <Link
                _text={{
                  fontSize: "xs",
                  fontWeight: "500",
                  color: "indigo.500",
                }}
                alignSelf="flex-end"
                mt="1"
              >
                Forget Password?
              </Link>
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
