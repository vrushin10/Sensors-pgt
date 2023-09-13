import "fetch";

export function Get(/*params: any*/) {
  const result = fetch("localhost", {
    method: "get",
  });
  return result;
}
