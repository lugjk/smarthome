/**
 * Learn more about using TypeScript with React Navigation:
 * https://reactnavigation.org/docs/typescript/
 */

import { BottomTabScreenProps } from "@react-navigation/bottom-tabs";
import {
  CompositeScreenProps,
  NavigatorScreenParams,
} from "@react-navigation/native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";

declare global {
  namespace ReactNavigation {
    interface RootParamList extends RootStackParamList {}
  }
}

export type RootTabParamList = {
  TabHome: { id: number };
  Setting: undefined;
};

export type GraphRoomParamList = {
  Graph1Room1: { id: number };
};

export type RootStackParamList = {
  Setting: undefined;
  Root: NavigatorScreenParams<RootTabParamList> | undefined;
  Modal: undefined;
  NotFound: undefined;
  Login: undefined;
  IDscreen: undefined;
  Menu: undefined;
  Graph1Room1: NavigatorScreenParams<GraphRoomParamList> | undefined;
  Graph2Room1: undefined;
  Graph3Room1: undefined;
  Graph4Room1: undefined;
  Graph5Room1: undefined;
  Graph6Room1: undefined;
  AllRoomScreen: undefined;
};

export type RootStackScreenProps<Screen extends keyof RootStackParamList> =
  NativeStackScreenProps<RootStackParamList, Screen>;

export type RootTabScreenProps<Screen extends keyof RootTabParamList> =
  CompositeScreenProps<
    BottomTabScreenProps<RootTabParamList, Screen>,
    NativeStackScreenProps<RootStackParamList>
  >;

export type GraphRoomScreenProps<Screen extends keyof GraphRoomParamList> =
  NativeStackScreenProps<GraphRoomParamList, Screen>;
