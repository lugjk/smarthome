import { StatusBar } from "expo-status-bar";
import { extendTheme, NativeBaseProvider } from "native-base";
import { SafeAreaProvider } from "react-native-safe-area-context";
import useCachedResources from "./hooks/useCachedResources";
import useColorScheme from "./hooks/useColorScheme";
import Navigation from "./navigation";
import { useState } from "react";
import { User } from "./models/models";

const theme = extendTheme({});
export default function App() {
  const isLoadingComplete = useCachedResources();
  const colorScheme = useColorScheme();
  const [user, setUser] = useState<User>({
    _id: "",
    token: "",
    email: "",
    username: ""
  })
  const value = {
    user: user,
    setUser: (user: User) => setUser(user)
  }

  if (!isLoadingComplete) {
    return null;
  } else {
    return (
      <NativeBaseProvider theme={theme}>
        <SafeAreaProvider>
            {/* <UserContext.Provider value={value}></UserContext.Provider> */}
            <Navigation colorScheme={colorScheme} />
          <StatusBar />
        </SafeAreaProvider>
      </NativeBaseProvider>
    );
  }
}
